%include	/usr/lib/rpm/macros.perl
Summary:	Frontend to rdesktop
Summary(pl.UTF-8):	Graficzny interfejs do obsługi rdesktop
Name:		xrdesktop
Version:	0.5
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://linux0wnsyou.com/xrdesktop/%{name}-%{version}.tar.gz
# Source0-md5:	3e96c6f54959b803e75cb10410d08c31
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://linux0wnsyou.com/xrdesktop/
Patch0:		%{name}-fix.patch
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	perl-gtk >= 0.7008
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	rdesktop >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple program, written in Perl using Gtk-Perl, as a frontend to
rdesktop.

%description -l pl.UTF-8
Graficzny interfejs do obsługi rdesktop, napisany w Perlu przy pomocy
Gtk-Perl.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install xrdesktop $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/xrdesktop
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
