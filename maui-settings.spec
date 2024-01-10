Name:		maui-settings
Version:	1.1.0
Release:	1
Summary:	Maui Settings Manager
Url:		https://github.com/Nitrux/maui-settings
Source0:	https://github.com/Nitrux/maui-settings/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

License:	 LGPL-3.0
Group:		Applications/Productivity/Shell/Maui
BuildRequires:  appstream
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit3)
BuildRequires:  cmake(MauiMan)
BuildRequires:  cmake(MauiCore)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:  cmake(CaskServer)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:  cmake(Qt5WaylandCompositor)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:  cmake(KDED)
BuildRequires:  qt5-qtbase-devel
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5ActivitiesStats)
BuildRequires:	cmake(KF5Completion)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(KF5Prison)
BuildRequires:	cmake(KF5Solid)
BuildRequires:  cmake(KF5Su)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5UnitConversion)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Runner)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:  cmake(KF5Wayland)

BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(Qt5QuickCompiler)

Requires: qml(org.mauicore.power)
Requires: cask-server
Requires: maui-shell

%description
Maui Settings Manager.

%prep
%autosetup -p1 -n %{name}-%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
