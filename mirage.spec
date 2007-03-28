# TODO
# - what python-pygtk it realy needs
# - cleanup and ready to go!
Summary:	Fast and simple image viewer in GTK+
Summary(pl.UTF-8):	Szybka i prosta przeglądarka obrazków w GTK+
Name:		mirage
Version:	0.8.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://download.berlios.de/mirageiv/%{name}-%{version}.tar.bz2
# Source0-md5:	a72f26fb2a60101816a50679729802e7
URL:		http://mirageiv.berlios.de/
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-pygtk-devel >= 2.6.0
Requires:	python-gnome
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
zależy tylko od PyGTK, Mirage jest idealne dla użytkowników,
którzy chcieliby utrzymać swój komputer odchudzony, a zarazem
posiadać dobrą przeglądarkę obrazów.

Cechy:
- Wspiera png, jpg, svg, xpm, gif, bmp, tiff i inne
- Przeglądanie wielu obrazków (bez wcześniejszego ładowania)
- Widok prezentacji i pełnoekranowy
- Obracanie, przybliżanie, odwracanie, zmiania rozmiaru i przycinanie
- Zachowywanie, kasowanie, zmiana nazwy
- Akcje definiowane przez użytkownika
- Dostęp z lini komend
- Konfigurowalny interfejs

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TRANSLATORS
%attr(755,root,root) %{_bindir}/mirage
%{py_sitedir}/mirage.pyc
%{py_sitedir}/imgfuncs.so
%{py_sitedir}/*.egg-info
%{_desktopdir}/mirage.desktop
%dir %{_datadir}/mirage
%{_datadir}/mirage/*.png
%{_pixmapsdir}/mirage.png
