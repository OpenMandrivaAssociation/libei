%define libname %mklibname ei
%define devname %mklibname -d ei

%define libeisname %mklibname eis
%define deveisname %mklibname -d eis

%define liboeffisname %mklibname oeffis
%define devoeffisname %mklibname -d oeffis

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
 
%description
libei is a library to Emulate Input. It allows clients to talk to
an EIS implementatation (Emulated Input Server), typically a Wayland compositor
and send input events via that connection. The EIS implementation
replays those events as if they came from physical devices.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
 
%description -n %{devname}
Library for Emulated Input Development Package.
 
%package utils
Summary:        Library for Emulated Input Utilities Package
Requires:	%{libname} = %{version}-%{release}
 
%description utils
Utilities to test and/or debug emulated input devices.
 
# libeis packages
%package -n %{libeisname}
Summary:        Library for Emulated Input Servers
 
%description -n %{libeisname}
libeis is a library to provide logical devices that other applications
can then use to emulate input. This library is typically used by
a Wayland compositor that provides an EIS implementation.
 
%package -n %{deveisname}
Summary:        Library for Emulated Input Serverse Development Package
Requires:	%{libeisname} = %{version}-%{release}
 
%description -n %{deveisname}
Library for Emulated Input Servers Development Package.
 
# liboeffis packages
%package -n %{liboeffisname}
Summary:        Library for XDG RemoteDesktop Portal Setup
 
%description -n %{liboeffisname}
liboeffis is a helper library to contact the XDG RemoteDesktop portal
and obtain an EIS socket through the portal.
 
%package -n %{devoeffisname}
Summary:        Library for XDG RemoteDesktop Portal Setup Development Package
Requires:	%{liboeffisname} = %{version}-%{release}
 
%description -n %{devoeffisname}
Library for XDG RemoteDesktop Portal Setup Development Package
 
%prep
%autosetup -S git
 
%build
%meson -Dtests=disabled -Ddocumentation='[]' -Dliboeffis=enabled
%meson_build
%install
%meson_install

%files -n %{libname}
%license COPYING
%{_libdir}/libei.so.1{,.*}
 
%files -n %{libeisname}
%license COPYING
%{_libdir}/libeis.so.1{,.*}
 
%files -n %{liboeffisname}
%license COPYING
%{_libdir}/liboeffis.so.1{,.*}
 
%files -n %{devname}
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/libei.h
%{_libdir}/libei.so
%{_libdir}/pkgconfig/libei-1.0.pc
 
%files -n %{deveisname}
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/libeis.h
%{_libdir}/libeis.so
%{_libdir}/pkgconfig/libeis-1.0.pc
 
%files -n %{devoeffisname}
%dir %{_includedir}/libei-1.0/
%{_includedir}/libei-1.0/liboeffis.h
%{_libdir}/liboeffis.so
%{_libdir}/pkgconfig/liboeffis-1.0.pc
 
%files utils
%{_bindir}/ei-debug-events
