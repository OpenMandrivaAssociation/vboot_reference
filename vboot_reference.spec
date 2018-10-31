%define debug_package %{nil}

Name: vboot_reference
Version: 0.2017.03.28
Release: 2
# From https://chromium.googlesource.com/chromiumos/platform/vboot_reference
Source0: %{name}-%{version}.tar.xz
Source1000: vboot_reference.rpmlintrc
# https://chromium-review.googlesource.com/461901
Patch0: vboot_reference/vboot_reference-openssl-1.1-clang-4.0.patch
Summary: Tools for working with ChromiumOS's vboot bootloader
URL: http://chromium.googlesource.com/chromiumos
License: BSD
Group: System/Base
BuildRequires: pkgconfig(openssl)

%description
Tools for working with ChromiumOS's vboot bootloader

You may need these tools to install OpenMandriva Lx on a Chromebook.

%prep
%setup -q
%apply_patches

%build
%make LIBDIR=%{_lib}

%install
%make install DESTDIR=%{buildroot}%{_prefix} LIBDIR=%{_lib}
chmod +x %{buildroot}%{_bindir}/*.sh

%files
%{_bindir}/*
%{_prefix}/default
%{_libdir}/pkgconfig/*
