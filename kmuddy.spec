Summary:	A MUD client powered by KDE
Name:		kmuddy
Version: 	1.0.1
Release: 	%mkrel 2
Source0: 	http://www.kmuddy.com/releases/devel/%{name}-%{version}.tar.gz
Patch1:		kmuddy-1.0-install-desktop.patch
License: 	GPLv2+
Group: 		Games/Other
Url: 		http://www.kmuddy.com
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
BuildRequires:	libmxp-devel
BuildRequires:	desktop-file-utils

%description 
KMuddy is a MUD client powered by KDE. It is a very powerful, fast,
feature-rich and easy to use MUD client.

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/kde4/*.so
%_kde_appsdir/%name
%_kde_applicationsdir/*.desktop
%_kde_iconsdir/*/*/*/*
%_kde_services/*.desktop
%_kde_servicetypes/*.desktop

#--------------------------------------------------------------------

%define major 1
%define libname %mklibname kmuddycore %major

%package -n %libname
Summary:	Shared libraries for kmuddy
Group:		Games/Other

%description -n %libname
This package contains shared libraries for kmuddy.

%files -n %libname
%defattr(-,root,root)
%_kde_libdir/*.so.%{major}*

#--------------------------------------------------------------------

%package devel
Summary:	Development files for kmuddy
Group:		Games/Other
Requires:	%libname = %version

%description devel
This package contains development files for kmuddy.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_includedir/%name

#--------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}
%patch1 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

desktop-file-install --vendor='' \
	--dir %buildroot%_kde_applicationsdir \
	--add-category='KDE;Qt;Game;RolePlaying' \
	%buildroot%_kde_applicationsdir/*.desktop

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
