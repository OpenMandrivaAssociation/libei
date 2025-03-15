%define major 0
%define libname %mklibname ei
%define devname %mklibname ei -d

Name:		libei
Version:	1.4.0
Release:	1
Source0:	https://gitlab.freedesktop.org/libinput/libei/-/archive/%{version}/libei-%{version}.tar.bz2
Summary:	Library for sending Emulated Input (EI) to a matching Emulated Input Server (EIS)
URL:		https://gitlab.freedesktop.org/libinput/libei
License:	MIT
Group:		System/Libraries
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	git-core
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	python
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(jinja2)
BuildSystem:	meson
BuildOption:	-Dtests=disabled

%description
libei is a library for Emulated Input, primarily aimed at the
Wayland stack. It provides three parts:

🥚 EI (Emulated Input) for the client side (libei)
🍦 EIS (Emulated Input Server) for the server side (libeis)
🚌 oeffis is an optional helper library for DBus communication
with the XDG RemoteDesktop portal (liboeffis)

The communication between EI and EIS happens over a UNIX socket via a custom
binary protocol. See the EI protocol documentation for details.

%prep
%autosetup -p1

%install -a
%libpackages

cat >>%{specpartsdir}/%{mklibname -d ei}.specpart <<EOF
%%dir %{_includedir}/libei-1.0
%{_includedir}/libei-1.0/libei.h
%{_libdir}/pkgconfig/libei-1.0.pc
EOF

cat >>%{specpartsdir}/%{mklibname -d eis}.specpart <<EOF
%{_includedir}/libei-1.0/libeis.h
%{_libdir}/pkgconfig/libeis-1.0.pc
EOF

cat >>%{specpartsdir}/%{mklibname -d oeffis}.specpart <<EOF
%{_includedir}/libei-1.0/liboeffis.h
%{_libdir}/pkgconfig/liboeffis-1.0.pc
EOF

%files
%{_bindir}/*
