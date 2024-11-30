Name:		maui-settings
Version:	1.1.0
Release:	2.20240730
Summary:	Maui Settings Manager
Url:		https://github.com/Nitrux/maui-settings
#Source0:	https://github.com/Nitrux/maui-settings/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source0:  maui-settings-master.tar.gz

License:	 LGPL-3.0
Group:		Applications/Productivity/Shell/Maui
BuildRequires:  appstream
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiMan)
BuildRequires:  cmake(MauiCore)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(CaskServer)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:  cmake(Qt6WaylandCompositor)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:  cmake(KDED)
#BuildRequires:  qt5-qtbase-devel
#BuildRequires:	qt5-qtgraphicaleffects
#BuildRequires:	qt5-qtdeclarative
#BuildRequires:	qt5-qtquickcontrols2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:	cmake(KF6Activities)
BuildRequires:	cmake(KF6ActivitiesStats)
BuildRequires:	cmake(KF6Completion)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6Init)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Prison)
BuildRequires:	cmake(KF6Solid)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Runner)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:  cmake(KF6Wayland)

BuildRequires:	cmake(KF6WidgetsAddons)

Requires: qml(org.mauicore.power)
Requires: cask-server
Requires: maui-shell

%description
Maui Settings Manager.

%prep
%autosetup -p1 -n %{name}-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
