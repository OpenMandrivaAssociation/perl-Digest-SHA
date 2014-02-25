%define debug_package %{nil}
%define	modname	Digest-SHA
%define modver 5.87

Summary:	Perl extension for SHA-1/224/256/384/512
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Digest/Digest-SHA-%{modver}.tar.gz

BuildRequires:	perl-devel

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, and SHA-512 message digests.  The module can handle all types of
input, including partial-byte data.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto/Digest
%{_mandir}/*/*
%{_bindir}/shasum



