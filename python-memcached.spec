Name:		python-memcached
Version:	1.47
Release:	%mkrel 1
Summary:	Python interface to memcached
Group:		Development/Python
License:	Python Software Foundation License
URL:		http://www.tummy.com/Community/software/python-memcached/
Source0:	ftp://ftp.tummy.com/pub/python-memcached/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
%py_requires	-d
BuildRequires:	python-setuptools

%description
This software is a 100%% Python interface to the memcached memory cache
daemon.  It is the client side software which allows storing values in one
or more, possibly remote, memcached servers.  Search google for memcached
for more information.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O2 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog PKG-INFO README
%{python_sitelib}/*



%changelog
* Tue Dec 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.47-1mdv2011.0
+ Revision: 625613
- update to new version 1.47

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.45-2mdv2011.0
+ Revision: 593933
- rebuild for py2.7

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.45-1mdv2010.1
+ Revision: 515907
- update to 1.45

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.43-3mdv2010.0
+ Revision: 442313
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.43-2mdv2009.1
+ Revision: 323789
- rebuild

* Tue Sep 16 2008 Luca Berra <bluca@mandriva.org> 1.43-1mdv2009.0
+ Revision: 285249
- import python-memcached


* Mon Sep 08 2008 Luca Berra <bluca@mandriva.org> 1.43-1mdv2008.1
- initial mandriva package
