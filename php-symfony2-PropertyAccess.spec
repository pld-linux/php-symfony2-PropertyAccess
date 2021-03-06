%define		package	PropertyAccess
%define		php_min_version 5.3.9
Summary:	Symfony2 PropertyAccess Component
Name:		php-symfony2-PropertyAccess
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	4a7adf09ea5714b20b846ccdd56436ce
URL:		https://symfony.com/doc/2.8/components/property_access.htmlintroduction.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides function to read and write from/to an object or array using a
simple string notation.

%prep
%setup -q -n property-access-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}

%{__rm} -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/PropertyAccess
%{php_data_dir}/Symfony/Component/PropertyAccess/*.php
%{php_data_dir}/Symfony/Component/PropertyAccess/Exception
