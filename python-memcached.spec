Name:		python-memcached
Version:	1.53
Release:	2
Summary:	Python interface to memcached

Group:		Development/Python
License:	Python Software Foundation License
URL:		https://www.tummy.com/Community/software/python-memcached/
Source0:	ftp://ftp.tummy.com:21/pub/python-memcached/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
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
python setup.py install -O2 --skip-build --root %{buildroot}

%clean

%files
%doc ChangeLog PKG-INFO 
%{py_puresitedir}/*
