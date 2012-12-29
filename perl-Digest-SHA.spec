%define	modname	Digest-SHA
%define	modver	5.62

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	6

Summary:	Perl extension for SHA-1/224/256/384/512
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Digest/%{modname}-%{modver}.tar.gz

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

%changelog
* Thu Dec 20 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.620.0-6
- rebuild against new perl-5.16.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 5.620.0-4mdv2012.0
+ Revision: 765189
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 5.620.0-3
+ Revision: 763705
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 5.620.0-2
+ Revision: 763241
- force it
- rebuild

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 5.620.0-1
+ Revision: 674799
- update to new version 5.62

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 5.610.0-2
+ Revision: 667122
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 5.610.0-1
+ Revision: 643377
- update to new version 5.61

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.500.0-1mdv2011.0
+ Revision: 622682
- update to new version 5.50

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 5.480.0-4mdv2011.0
+ Revision: 564430
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 5.480.0-3mdv2011.0
+ Revision: 555246
- rebuild
- rebuild for 5.12

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 5.480.0-1mdv2010.1
+ Revision: 486310
- update to 5.48

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 5.470.0-1mdv2010.0
+ Revision: 403152
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 5.47-3mdv2009.1
+ Revision: 351719
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 5.47-2mdv2009.0
+ Revision: 265357
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.47-1mdv2009.0
+ Revision: 201852
- update to new version 5.47

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.46-1mdv2009.0
+ Revision: 194850
- update to new version 5.46
- update to new version 5.46

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 5.45-2mdv2008.1
+ Revision: 152067
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.45-1mdv2008.0
+ Revision: 46523
- update to new version 5.45


* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.44-1mdv2007.0
+ Revision: 86575
- new version
- Import perl-Digest-SHA

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.43-1mdv2007.0
- New version 5.43

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.42-1mdv2007.0
- New version 5.42

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.41-1mdv2007.0
- New release 5.41
- HTTP source URL

* Mon May 29 2006 Scott Karns <scottk@mandriva.org> 5.39-1mdv2007.0
- New release 5.39

* Fri May 26 2006 Scott Karns <scottk@mandriva.org> 5.38-1mdv2007.0
- New release 5.38
- Removed BuildRequires perl(Module::Build)

* Thu May 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.37-1mdk
- New release 5.37

* Mon May 08 2006 Scott Karns <scottk@mandriva.org> 5.36-1mdk
- New release 5.36

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.34-1mdk
- New release 5.34
- fix optimisations

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.32-1mdk
- New release 5.32
- spec cleanup
- fix directory ownership
- better summary

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.31-1mdk
- New release 5.31

* Fri Sep 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.30-1mdk
- 5.30

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.29-1mdk
- new version
- fix sources url for rpmbuildupdate

* Thu Jul 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.28-1mdk
- 5.28

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 5.26-1mdk
- initial Mandriva package

