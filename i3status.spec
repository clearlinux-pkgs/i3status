#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : i3status
Version  : 2.11
Release  : 3
URL      : https://i3wm.org/i3status/i3status-2.11.tar.bz2
Source0  : https://i3wm.org/i3status/i3status-2.11.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: i3status-bin
Requires: i3status-doc
Requires: i3status-data
BuildRequires : libnl-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libconfuse)
BuildRequires : pkgconfig(libpulse)
BuildRequires : yajl-dev

%description
# i3status
## Description
i3status is a small program (about 1500 SLOC) for generating a status bar for
i3bar, dzen2, xmobar or similar programs. It is designed to be very efficient by
issuing a very small number of system calls, as one generally wants to update
such a status line every second. This ensures that even under high load, your
status bar is updated correctly. Also, it saves a bit of energy by not hogging
your CPU as much as spawning the corresponding amount of shell commands would.

%package bin
Summary: bin components for the i3status package.
Group: Binaries
Requires: i3status-data

%description bin
bin components for the i3status package.


%package data
Summary: data components for the i3status package.
Group: Data

%description data
data components for the i3status package.


%package doc
Summary: doc components for the i3status package.
Group: Documentation

%description doc
doc components for the i3status package.


%prep
%setup -q -n i3status-2.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525466430
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1525466430
rm -rf %{buildroot}
%make_install
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/xdg/i3status
install -m 644 i3status.conf %{buildroot}/usr/share/xdg/i3status/config
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/i3status

%files data
%defattr(-,root,root,-)
/usr/share/xdg/i3status/config

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
