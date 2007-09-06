Summary:	X.org video driver for Cyrix video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Cyrix
Name:		xorg-driver-video-cyrix
Version:	1.1.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-cyrix-%{version}.tar.bz2
# Source0-md5:	02ed7d5215610a3463a0307b30bb5425
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
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-cyrix < 1:7.0.0
Obsoletes:	XFree86-Cyrix
Obsoletes:	XFree86-driver-cyrix < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Cyrix MediaGX (now Natsemi Geode) series of
video processors. This driver supports the MediaGX, MediaGXi and
MediaGXm processors, as well as the Natsemi 'Geode' branded
processors. It supports the CS5510, CS5520, CS5530 and CS5530A
companion chips.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych z serii Cyrix MediaGX
(teraz Natsemi Geode). Ten sterownik obsługuje układy MediaGX,
MediaGXi, MediaGXm, a także firmowane jako Natsemi "Geode". Obsługuje
układy towarzyszące CS5510, CS5520, CS5530 i CS5530A.

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
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cyrix_drv.so
%{_mandir}/man4/cyrix.4*
