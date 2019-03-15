%define         appdir      /opt/nagiosmsg

Name:		nagiosmsg
Version:	0.0.3
Release:	1%{?dist}
Summary:	Send custom message

Group:		Monitoring
License:	MIT
Source0:	%{name}-%{version}.tar.gz
Requires:	python-jinja2
Requires:	PyYAML

%description

Python version of a set of php scripts (https://github.com/heiniha/Nagios-Responsive-HTML-Email-Notifications).


%prep
%setup -q


%install

%{__mkdir_p} %{buildroot}/%{appdir}/bin
%{__mkdir_p} %{buildroot}/%{appdir}/etc
%{__mkdir_p} %{buildroot}/%{appdir}/templates
%{__mkdir_p} %{buildroot}/%{appdir}/
%{__mkdir_p} %{buildroot}/%{_defaultdocdir}/%{name}

for filen in bin/*
do
  %{__install} -m755 $filen %{buildroot}/%{appdir}/$filen
done

for filen in templates/* etc/*
do
  %{__install} -m644 $filen %{buildroot}/%{appdir}/$filen
done

pushd docs
for filen in *
do
  %{__install} -m644 $filen %{buildroot}/%{_defaultdocdir}/%{name}/$filen
done



%files
%doc %{_defaultdocdir}/%{name}/*
%{appdir}/bin/*
%{appdir}/templates/*
%config(noreplace) %{appdir}/etc/*

%changelog
* Sat Mar 16 2019 John van Zantvoort <john@vanzantvoort.org> 0.0.3-1
- etc should exist (john@vanzantvoort.org)

* Sat Mar 16 2019 John van Zantvoort <john@vanzantvoort.org> 0.0.2-1
- first version

