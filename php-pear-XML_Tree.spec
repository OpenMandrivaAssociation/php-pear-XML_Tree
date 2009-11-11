%define		_class		XML
%define		_subclass	Tree
%define		upstream_name	%{_class}_%{_subclass}
%define		_rc		RC2

Name:		php-pear-%{upstream_name}
Version:	2.0.0
Summary:	Represent XML data in a tree structure
Release:	%mkrel 12
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_Tree/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{_rc}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Allows for the building of XML data structures using a tree
representation, without the need for an extension like DOMXML.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{_rc}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}%{_rc}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}%{_rc}/README.txt
%doc %{upstream_name}-%{version}%{_rc}/docs
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
