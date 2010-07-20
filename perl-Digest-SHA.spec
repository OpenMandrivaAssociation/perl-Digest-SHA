%define	upstream_name	 Digest-SHA
%define upstream_version 5.48

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Perl extension for SHA-1/224/256/384/512
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, and SHA-512 message digests.  The module can handle all types of
input, including partial-byte data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto/Digest
%{_mandir}/*/*
%{_bindir}/shasum
