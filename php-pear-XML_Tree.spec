%define		_class		XML
%define		_subclass	Tree
%define		upstream_name	%{_class}_%{_subclass}
%define		_rc		RC2

Name:		php-pear-%{upstream_name}
Version:	2.0.0
Summary:	Represent XML data in a tree structure
Release:	%mkrel 15
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
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}%{_rc}/README.txt
%doc %{upstream_name}-%{version}%{_rc}/docs
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-15mdv2012.0
+ Revision: 742313
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-14
+ Revision: 679614
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-13mdv2011.0
+ Revision: 613800
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-12mdv2010.1
+ Revision: 464969
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-11mdv2010.0
+ Revision: 441768
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-10mdv2009.1
+ Revision: 322992
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-9mdv2009.0
+ Revision: 237172
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-8mdv2007.0
+ Revision: 82946
- Import php-pear-XML_Tree

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdk
- initial Mandriva package (PLD import)

