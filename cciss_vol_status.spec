Summary:	HP Smart Array Status Display
Name:		cciss_vol_status
Version:	1.11
Release:        1
Group:		System/Kernel and hardware
License:	GPLv2
Source0:	https://sourceforge.net/projects/cciss/files/cciss_vol_status/%{name}-%{version}.tar.gz
BuildRequires:	kernel-source
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Show status of logical drives attached to HP Smart Array controllers.

%prep

%setup -q

%build
autoreconf -fis

%configure2_5x

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 cciss_vol_status %{buildroot}%{_sbindir}/
install -m0644 cciss_vol_status.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%{_sbindir}/cciss_vol_status
%{_mandir}/man8/cciss_vol_status.8*



%changelog
* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.09-1mdv2011.0
+ Revision: 645061
- update to new version 1.09

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.03-3mdv2011.0
+ Revision: 616949
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2010.0
+ Revision: 424750
- rebuild

* Mon Sep 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03-1mdv2009.0
+ Revision: 282672
- import cciss_vol_status


* Mon Sep 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03-1mdv2009.0
- initial Mandriva package (opensuse import)


