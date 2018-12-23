Name:		nagios-plugins-iostat
Version:	0.0.1
Release:	1%{?dist}
Summary:	Get iostats

Group:		Monitoring
License:	MIT
Source0:	%{name}-%{version}.tar.gz

%description
TBD

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%{__mkdir_p} %{buildroot}/%{_libdir}/nagios/plugins

%{__install} -m755 check_iostat %{buildroot}/%{_libdir}/nagios/plugins/check_iostat


%files
%{_libdir}/nagios/plugins/check_iostat



%changelog

