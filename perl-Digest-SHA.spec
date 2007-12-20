%define	module	Digest-SHA
%define	name	perl-%{module}
%define	modprefix Digest
%define	version	5.45
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for SHA-1/224/256/384/512
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, and SHA-512 message digests.  The module can handle all types of
input, including partial-byte data.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/%{modprefix}
%{perl_vendorarch}/auto/%{modprefix}
%{_mandir}/*/*
%{_bindir}/shasum


