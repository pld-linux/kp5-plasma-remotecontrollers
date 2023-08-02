#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.7
%define		qtver		5.15.2
%define		kpname		plasma-remotecontrollers
%define		kf5ver		5.39.0

Summary:	plasma-remotecontrollers
Name:		kp5-%{kpname}
Version:	5.27.7
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	fb25df16ef388f7dbfc163911e7828be
Patch0:		udev.patch
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.15.0
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5WaylandClient-devel
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext
BuildRequires:	kf5-kcmutils-devel >= 5.68.0
BuildRequires:	kf5-kconfig-devel >= 5.99.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.99.0
BuildRequires:	kf5-kdeclarative-devel >= 5.68.0
BuildRequires:	kf5-ki18n-devel >= 5.68.0
BuildRequires:	kf5-kitemmodels-devel >= 5.98.0
BuildRequires:	kf5-knotifications-devel >= 5.68.0
BuildRequires:	kf5-kpackage-devel >= 5.68.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.68.0
BuildRequires:	kf5-plasma-wayland-protocols-devel >= 1.10.0
BuildRequires:	kf5-solid-devel >= 5.68.0
BuildRequires:	kp5-kscreenlocker-devel >= %{version}
BuildRequires:	kp5-plasma-workspace-devel >= %{version}
BuildRequires:	libcec-devel
BuildRequires:	libevdev-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This project translates events from various input devices to
keypresses on a keyboard and pointer events (mouse movement).

%description -l pl.UTF-8

%prep
%setup -q -n %{kpname}-%{version}
%patch0 -p1

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/autostart/org.kde.plasma-remotecontrollers.desktop
/etc/xdg/plasma-remotecontrollersrc
%attr(755,root,root) %{_bindir}/plasma-remotecontrollers
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_remotecontrollers.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/remotecontrollers
%{_libdir}/qt5/qml/org/kde/plasma/remotecontrollers/qmldir
/lib/udev/rules.d/40-uinput.rules
%{_desktopdir}/org.kde.plasma-remotecontrollers.desktop
%{_datadir}/knotifications5/plasma-remotecontrollers.notifyrc
%dir %{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers
%dir %{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents
%dir %{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/+mediacenter
%dir %{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/delegates
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/+mediacenter/DeviceMap.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/+mediacenter/DeviceSetupView.qml
%dir %{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/+mediacenter/delegates
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/+mediacenter/delegates/DeviceDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/+mediacenter/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/DeviceMap.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/DeviceSetupView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/delegates/DeviceDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/delegates/MapButtonDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers/metadata.json
%{_datadir}/kservices5/kcm_mediacenter_remotecontrollers.desktop
%{_datadir}/metainfo/org.kde.plasma.remotecontrollers.metainfo.xml
%{_datadir}/qlogging-categories5/plasma-remotecontrollers.categories
%{_datadir}/dbus-1/interfaces/org.kde.plasma.remotecontrollers.CEC.xml
%{_datadir}/dbus-1/interfaces/org.kde.plasma.remotecontrollers.ControllerManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.plasma.remotecontrollers.EVDEV.xml
