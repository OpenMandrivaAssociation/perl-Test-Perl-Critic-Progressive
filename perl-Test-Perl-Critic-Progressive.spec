%define upstream_name    Test-Perl-Critic-Progressive
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Gradually enforce coding standards
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(English)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Perl::Critic::Utils)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildArch:	noarch

%description
Applying coding standards to large amounts of legacy code is a daunting
task. Often times, legacy code is so non-compliant that it seems downright
impossible. But, if you consistently chip away at the problem, you will
eventually succeed! Test::Perl::Critic::Progressive uses the the
Perl::Critic manpage engine to prevent further deterioration of your code
and *gradually* steer it towards conforming with your chosen coding
standards.

The most effective way to use Test::Perl::Critic::Progressive is as a unit
test that is run under a continuous-integration system like CruiseControl
or AntHill. Each time a developer commits changes to the code, this test
will fail and the build will break unless it has the same (or fewer)
Perl::Critic violations than the last successful test.

See the the "NOTES" manpage for more details about how this test works.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 656828
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 572894
- import perl-Test-Perl-Critic-Progressive

