Summary:	A simple font management application for Gtk+ Desktop Environments
Summary(pl.UTF-8):	Prosty manager czcionek dla środowisk graficznych opartych na Gtk+
Name:		font-manager
Version:	0.8.8
Release:	1
License:	GPL-3.0-or-later
URL:		https://fontmanager.github.io/
Source0:	https://github.com/FontManager/font-manager/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	9dbcaf606df347b3daba338cce495846
BuildRequires:	Thunar-devel
BuildRequires:	appstream-glib
BuildRequires:	cinnamon-nemo-devel
BuildRequires:	fontconfig-devel >= 2.12
BuildRequires:	freetype-devel
BuildRequires:	gettext
BuildRequires:	glib2-devel >= 2.44
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-webkit4-devel >= 2.13.90
BuildRequires:	json-glib-devel
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel
BuildRequires:	meson
BuildRequires:	nautilus-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	vala >= 0.42
BuildRequires:	yelp-tools
Requires:	%{name}-common
Requires:	font-viewer
Requires:	fontconfig
Requires:	gtk-webkit4

%description
Font Manager is intended to provide a way for average users to easily
manage desktop fonts, without having to resort to command line tools
or editing configuration files by hand. While designed primarily with
the Gnome Desktop Environment in mind, it should work well with other
Gtk+ desktop environments.

Font Manager is NOT a professional-grade font management solution.

%description -l pl.UTF-8
Font Manager ma na celu umożliwienie przeciętnym użytkownikom łatwego
zarządzania czcionkami w środowisku graficznym bez konieczności
uciekania się do narzędzi wiersza poleceń lub ręcznego edytowania
plików konfiguracyjnych. Chociaż zaprojektowany głównie z myślą o
środowisku graficznym Gnome, powinien dobrze współpracować z innymi
środowiskami graficznymi Gtk+.

Menedżer czcionek NIE jest profesjonalnym rozwiązaniem do zarządzania
czcionkami.

%package -n %{name}-common
Summary:	Common files used by font-manager
Summary(pl.UTF-8):	Wspólne pliki używane przez font-manager

%description -n %{name}-common
This package contains common files such as libraries. These files are
required by font-manager and font-viewer.

%description -n %{name}-common -l pl.UTF-8
Ten pakiet zawiera pliki wspólne, wymagane przez programy font-manager
i font-viewer.

%package -n font-viewer
Summary:	Full featured font file preview application for GTK+ Desktop Environments
Summary(pl.UTF-8):	W pełni funkcjonalna aplikacja do podglądu plików czcionek dla środowisk graficznych GTK+
Requires:	%{name}-common >= %{version}

%description -n font-viewer
This package contains the font-viewer component of font-manager.

%description -n font-viewer -l pl.UTF-8
Ten pakiet zawiera komponent font-viewer pakietu font-manager.

%package -n nautilus-%{name}
Summary:	Nautilus extension for Font Manager
Summary(pl.UTF-8):	Rozszerzenie Font Manager dla Nautilusa
Requires:	%{name}-common >= %{version}
Requires:	font-viewer >= %{version}

%description -n nautilus-%{name}
This package provides integration with the Nautilus file manager.

%description -n nautilus-%{name} -l pl.UTF-8
Ten pakiet pozwala na integrację FontManager'a z managerem plików
Nautilus.

%package -n nemo-%{name}
Summary:	Nemo extension for Font Manager
Summary(pl.UTF-8):	Rozszerzenie Font Manager dla Nemo
Requires:	%{name}-common >= %{version}
Requires:	font-viewer >= %{version}

%description -n nemo-%{name}
This package provides integration with the Nemo file manager.

%description -n nemo-%{name} -l pl.UTF-8
Ten pakiet pozwala na integrację FontManager'a z managerem plików
Nemo.

%package -n thunar-%{name}
Summary:	Thunar extension for Font Manager
Summary(pl.UTF-8):	Rozszerzenie Font Manager dla Thunara
Requires:	%{name}-common >= %{version}
Requires:	font-viewer >= %{version}

%description -n thunar-%{name}
This package provides integration with the Thunar file manager.

%description -n thunar-%{name} -l pl.UTF-8
Ten pakiet pozwala na integrację FontManager'a z managerem plików
Thunar.

%package gnome-shell-search
Summary:	Package provideing font-manager support in gnome shell search
Summary(pl.UTF-8):	Pakiet pozwalający przeszukiwanie font-manager'a z poziomu wyszukiwarki gnome shell
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description gnome-shell-search
This package integrates Font-Manager with gnome shell search tool.

%description gnome-shell-search -l pl.UTF-8
Ten pakiet integruje Font-Manager'a z wyszukiwarką gnome shell

%prep
%setup -q

%build
%meson -Dnautilus=True -Dnemo=True -Dthunar=true -Dreproducible=true build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/libfontmanager.so
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/{nb_NO,zh_Hans,zh_Hant,zh_Hant_HK}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/nb_NO

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.FontManager.appdata.xml
%{_desktopdir}/org.gnome.FontManager.desktop
%{_datadir}/dbus-1/services/org.gnome.FontManager.service
%{_datadir}/glib-2.0/schemas/org.gnome.FontManager.gschema.xml
%{_iconsdir}/hicolor/128x128/apps/org.gnome.FontManager.png
%{_iconsdir}/hicolor/256x256/apps/org.gnome.FontManager.png
%{_mandir}/man1/%{name}.*

%files -n %{name}-common
%defattr(644,root,root,755)
%doc COPYING
%{_libdir}/%{name}

%files -n font-viewer
%defattr(644,root,root,755)
%dir %{_libexecdir}/%{name}
%attr(755,root,root) %{_libexecdir}/%{name}/font-viewer
%{_datadir}/metainfo/org.gnome.FontViewer.appdata.xml
%{_desktopdir}/org.gnome.FontViewer.desktop
%{_datadir}/dbus-1/services/org.gnome.FontViewer.service
%{_datadir}/glib-2.0/schemas/org.gnome.FontViewer.gschema.xml
%{_iconsdir}/hicolor/128x128/apps/org.gnome.FontViewer.png
%{_iconsdir}/hicolor/256x256/apps/org.gnome.FontViewer.png

%files -n nautilus-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/nautilus-%{name}.so

%files -n nemo-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/nemo-%{name}.so

%files -n thunar-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/thunarx-3/thunar-%{name}.so

%files gnome-shell-search
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/search-providers/org.gnome.FontManager.SearchProvider.ini
