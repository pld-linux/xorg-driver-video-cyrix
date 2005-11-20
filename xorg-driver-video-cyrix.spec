Summary:	X.org video driver for Cyrix video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych Cyrix
Name:		xorg-driver-video-cyrix
Version:	1.0.0.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-cyrix-%{version}.tar.bz2
# Source0-md5:	c449d9c43cd3d8cf1ebb7c5a9d159d3d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Cyrix MediaGX (now Natsemi Geode) series of
video processors. This driver supports the MediaGX, MediaGXi and
MediaGXm processors, as well as the Natsemi 'Geode' branded
processors. It supports the CS5510, CS5520, CS5530 and CS5530A
companion chips.

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych z serii Cyrix MediaGX
(teraz Natsemi Geode). Ten sterownik obs³uguje uk³ady MediaGX,
MediaGXi, MediaGXm, a tak¿e firmowane jako Natsemi "Geode". Obs³uguje
uk³ady towarzysz±ce CS5510, CS5520, CS5530 i CS5530A.

%prep
%setup -q -n xf86-video-cyrix-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cyrix_drv.so
%{_mandir}/man4/cyrix.4x*
