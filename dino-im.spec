%define oname dino
Name:		dino-im
Version:	0.4.0
Release:	1
Group:		Networking/Chat
License:	GPLv3
Summary:	Modern XMPP ("Jabber") Chat Client using GTK+/Vala
URL:		https://github.com/dino/dino
Source0:	https://github.com/dino/dino/releases/download/v%{version}/dino-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	vala
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(gpgme)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gspell-1)
#BuildRequires:	pkgconfig(gstreamermm-1.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libadwaita-1)
#BuildRequires:	pkgconfig(libsignal-protocol-c)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libsrtp2)
BuildRequires:	pkgconfig(nice)
BuildRequires:	pkgconfig(webrtc-audio-processing)

%description
A modern XMPP ("Jabber") chat client using GTK+/Vala.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake -GNinja
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{oname}
%find_lang %{oname}-omemo
%find_lang %{oname}-openpgp

rm -rf %{buildroot}%{_includedir}/*.h
rm -rf %{buildroot}%{_libdir}/*.so
rm -rf %{buildroot}%{_datadir}/vala/


%files -f %{oname}.lang -f %{oname}-omemo.lang -f %{oname}-openpgp.lang
%license LICENSE
%doc README.md
%{_bindir}/%{oname}
%{_datadir}/applications/im.%{oname}.Dino.desktop
%{_datadir}/dbus-1/services/im.%{oname}.Dino.service
%{_iconsdir}/hicolor/scalable/apps/im.%{oname}.Dino.svg
%{_iconsdir}/hicolor/symbolic/apps/im.%{oname}.Dino-symbolic.svg
%{_metainfodir}/im.%{oname}.Dino.appdata.xml
%{_libdir}/%{oname}/
%{_libdir}/libdino.so.0*
%{_libdir}/libqlite.so.0*
%{_libdir}/libxmpp-vala.so.0*
%{_libdir}/libcrypto-vala.so.0*
