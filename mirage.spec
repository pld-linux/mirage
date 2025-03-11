# TODO
# - cleanup and ready to go!
# - desktop integration (file association)
Summary:	Fast and simple image viewer in GTK+
Summary(pl.UTF-8):	Szybka i prosta przeglądarka obrazków w GTK+
Name:		mirage
Version:	0.9.5.2
Release:	5
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	http://download.berlios.de/mirageiv/%{name}-%{version}.tar.bz2
# Source0-md5:	92191a4496b0a50486ed7299baf6729f
Patch0:		prevmouse-not-defined-with-click.patch
Patch1:		glib241-init-workaround.patch
Patch2:		py3-gtk3.patch
Patch3:		pep632-distutils-port.patch
URL:		http://mirageiv.berlios.de/
BuildRequires:	gtk+3-devel
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	gtk+3
Requires:	python3-pygobject3
Requires:	python3-pycairo
Requires:	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mirage is a fast and simple GTK+ image viewer. Because it depends only
on PyGTK, Mirage is ideal for users who wish to keep their computers
lean while still having a clean image viewer.

Features:
- Supports png, jpg, svg, xpm, gif, bmp, tiff, and others
- Cycling through multiple images (with preloading)
- Slideshow and fullscreen modes
- Rotating, zooming, flipping, resizing, cropping
- Saving, deleting, renaming
- Custom actions
- Command-line access
- Configurable interface

%description -l pl.UTF-8
Mirage to szybka i prosta przeglądarka obrazków w GTK+. Ponieważ
zależy tylko od PyGTK, Mirage jest idealne dla użytkowników, którzy
chcieliby utrzymać swój komputer odchudzony, a zarazem posiadać dobrą
przeglądarkę obrazów.

Cechy:
- Wspiera png, jpg, svg, xpm, gif, bmp, tiff i inne
- Przeglądanie wielu obrazków (bez wcześniejszego ładowania)
- Widok prezentacji i pełnoekranowy
- Obracanie, przybliżanie, odwracanie, zmiana rozmiaru i przycinanie
- Zachowywanie, kasowanie, zmiana nazwy
- Akcje definiowane przez użytkownika
- Dostęp z linii poleceń
- Konfigurowalny interfejs

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

# Don't remove rebuilt files!
%{__sed} -i -e '/Cleanup/,$d' setup.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/{CHANGELOG,COPYING,README,TODO,TRANSLATORS}

# ukranian, seems not supported
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ua

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TRANSLATORS
%attr(755,root,root) %{_bindir}/mirage
%{py3_sitedir}/__pycache__/*.py*
%{py3_sitedir}/mirage.py
%attr(755,root,root) %{py3_sitedir}/imgfuncs.*.so
%attr(755,root,root) %{py3_sitedir}/xmouse.*.so
%{py3_sitedir}/*.egg-info
%{_desktopdir}/mirage.desktop
%dir %{_datadir}/mirage
%{_datadir}/mirage/*.png
%{_pixmapsdir}/mirage.png
