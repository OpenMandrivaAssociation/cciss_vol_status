Summary:	HP Smart Array Status Display
Name:		cciss_vol_status
Version:	1.09
Release:        %mkrel 1
Group:		System/Kernel and hardware
License:	GPLv2
Source0:	http://prdownloads.sourceforge.net/cciss/%{name}-%{version}.tar.gz
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

