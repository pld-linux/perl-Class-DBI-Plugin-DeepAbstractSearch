#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Class
%define	pnam	DBI-Plugin-DeepAbstractSearch
Summary:	Class::DBI::Plugin::DeepAbstractSearch - deep_search_where() for Class::DBI
#Summary(pl.UTF-8):	
Name:		perl-Class-DBI-Plugin-DeepAbstractSearch
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4753aff910ba9080dfa4040ed834d4e
URL:		http://search.cpan.org/dist/Class-DBI-Plugin-DeepAbstractSearch/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::DBI::Plugin) >= 0.02
BuildRequires:	perl-Class-DBI >= 0.96
BuildRequires:	perl-SQL-Abstract >= 1.18
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin provides a SQL::Abstract search method for Class::DBI.
It is similar to Class::DBI::AbstractSearch, but allows you to search
and sort by fields from joined tables.

Note: When searching and sorting by the fields of the current class only,
it is more efficient to use Class::DBI::AbstractSearch.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/Plugin/*.pm
%{_mandir}/man3/*
