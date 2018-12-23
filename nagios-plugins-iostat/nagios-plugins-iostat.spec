Name:		nagios-plugins-iostat
Version:	0.0.1
Release:	1%{?dist}
Summary:	

Group:		
License:	
URL:		
Source0:	

BuildRequires:	
Requires:	

%description


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

