%define version      0.0.4
%define release      %mkrel 1

%define scim_version 1.4.1

Name:		scim-panel-gnome
Summary:	SCIM panel for GNOME
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://www.homa.ne.jp/~ashie/linux/files
Source0:	http://www.homa.ne.jp/~ashie/linux/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	scim >= %{scim_version}
BuildRequires:  scim-devel >= %{scim_version}
BuildRequires:  gnomeui2-devel gnome-panel-devel

%description
scim-panel-gnome is a SCIM panel for GNOME.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
# change config to use scim-panel-gnome
if [ $1 = 1 ]; then
   cd /etc/scim/
   perl -i.bak -p -e 's/scim-panel-gtk/scim-panel-gnome/g' global
   cd -
fi

%postun
# restore config
if [ $1 = 0 ]; then
   cd /etc/scim/
   mv -f global.bak global
   cd -
fi


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/gnome-2.0/ui/*.xml
%{_libdir}/bonobo/servers/*.server
%{_libdir}/scim-1.0/scim-panel-gnome
%{_libdir}/scim-applet
