Name:           libei
Version:        1.1.0
Release:        1
Summary:        Library for Emulated Input
 
License:        MIT
URL:            http://gitlab.freedesktop.org/libinput/libei
Source0:        https://gitlab.freedesktop.org/libinput/libei/-/archive/%{version}/libei-%{version}.tar.bz2
 
BuildRequires:  git-core
BuildRequires:  libxml2
BuildRequires:  meson
BuildRequires:  python
BuildRequires:  python-attrs
BuildRequires:  python-jinja2
BuildRequires:  pkgconfig(libsystemd)
 
# libei packages
%description
libei is a library to Emulate Input. It allows clients to talk to
an EIS implementatation (Emulated Input Server), typically a Wayland compositor
and send input events via that connection. The EIS implementation
replays those events as if they came from physical devices.
 
%package devel
Summary:        Library for Emulated Input Development Package
Requires:       libei%{?_isa} = %{version}-%{release}
 
%description devel
Library for Emulated Input Development Package.
 
%package utils
Summary:        Library for Emulated Input Utilities Package
Requires:       libei%{?_isa} = %{version}-%{release}
 
%description utils
Utilities to test and/or debug emulated input devices.
 
# libeis packages
%package -n libeis
Summary:        Library for Emulated Input Servers
 
%description -n libeis
libeis is a library to provide logical devices that other applications
can then use to emulate input. This library is typically used by
a Wayland compositor that provides an EIS implementation.
 
%package -n libeis-devel
Summary:        Library for Emulated Input Serverse Development Package
Requires:       libeis%{?_isa} = %{version}-%{release}
 
%description -n libeis-devel
Library for Emulated Input Servers Development Package.
 
# liboeffis packages
%package -n liboeffis
Summary:        Library for XDG RemoteDesktop Portal Setup
 
%description -n liboeffis
liboeffis is a helper library to contact the XDG RemoteDesktop portal
and obtain an EIS socket through the portal.
 
%package -n liboeffis-devel
Summary:        Library for XDG RemoteDesktop Portal Setup Development Package
Requires:       liboeffis%{?_isa} = %{version}-%{release}
 
%description -n liboeffis-devel
Library for XDG RemoteDesktop Portal Setup Development Package
 
%prep
%autosetup -S git
 
%build
%meson -Dtests=disabled -Ddocumentation='[]' -Dliboeffis=enabled
%meson_build
%install
%meson_install
%files
%license COPYING
%{_libdir}/libei.so.1{,.*}
 
%files -n libeis
%license COPYING
%{_libdir}/libeis.so.1{,.*}
 
%files -n liboeffis
%license COPYING
%{_libdir}/liboeffis.so.1{,.*}
 
%files devel
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/libei.h
%{_libdir}/libei.so
%{_libdir}/pkgconfig/libei-1.0.pc
 
%files -n libeis-devel
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/libeis.h
%{_libdir}/libeis.so
%{_libdir}/pkgconfig/libeis-1.0.pc
 
%files -n liboeffis-devel
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/liboeffis.h
%{_libdir}/liboeffis.so
%{_libdir}/pkgconfig/liboeffis-1.0.pc
 
%files utils
%{_bindir}/ei-debug-events
