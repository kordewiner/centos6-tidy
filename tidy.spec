Name:    tidy
Summary: HTML Tidy with HTML5 support
Version: 5.2.0
Release: 0.1%{?dist}

Group:   Applications/Text
License: W3C
URL:     http://www.html-tidy.org/
BuildRoot: %{_tmppath}/%{name}-html5-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: https://github.com/htacg/%{name}-html5/archive/%{version}.tar.gz


%description
The granddaddy of HTML tools. Tidy is a console application. It corrects 
and cleans up HTML and XML documents by fixing markup errors and 
upgrading legacy code to modern standards.


%prep
%setup -qn %{name}-html5-%{version}


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/tidy
%{_mandir}/man1/tidy.1.gz
%{_includedir}/*.h
%{_libdir}/*
%doc README/LICENSE.md
%doc README/README.md
%doc README/RELEASE.html


%changelog

* Fri Oct 05 2016 Hnr Kordewiner <hnr@eilbek.net> - 5.2.0-0.1
- Latest

* Fri May 22 2015 Hnr Kordewiner <hnr@eilbek.net> - 4.9.28-0.1
- First build.
