Name:		python-memcached
Version:	1.45
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

