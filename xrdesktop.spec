%include	/usr/lib/rpm/macros.perl
Summary:	Frontend to rdesktop
Summary(pl):	Graficzny interfejs do obs³ugi rdesktop
Name:		xrdesktop
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://linux0wnsyou.com/xrdesktop/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://linux0wnsyou.com/xrdesktop/
Patch0:		%{name}-fix.patch
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.6
BuildRequires:	perl-gtk >= 0.7008
Requires:	rdesktop >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Simple program, written in perl using gtk-perl, as a frontend to
rdesktop.

%description -l pl
Graficzny interfejs do obs³ugi rdesktop, napisany w perlu przy pomocy
gtk-perl

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Network}

install xrdesktop $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/xrdesktop
%{_applnkdir}/Network/xrdesktop.desktop
