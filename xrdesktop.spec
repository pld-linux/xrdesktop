%include	/usr/lib/rpm/macros.perl
Summary:	Frontend to rdesktop
Summary(pl):	Graficzny interfejs do obs³ugi rdesktop
Name:		xrdesktop
Version:	0.4
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://linux0wnsyou.com/xrdesktop/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://linux0wnsyou.com/xrdesktop/
Patch0:		%{name}-fix.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-gtk >= 0.7008
BuildRequires:	rpm-perlprov
Requires:	rdesktop >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Simple program, written in perl using gtk-perl, as a frontend to
rdesktop.

%description -l pl
Graficzny interfejs do obs³ugi rdesktop, napisany w Perlu przy pomocy
Gtk-Perl.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Network,%{_pixmapsdir}}

install xrdesktop $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/xrdesktop
%{_applnkdir}/Network/xrdesktop.desktop
%{_pixmapsdir}/*.png
