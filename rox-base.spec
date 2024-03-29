Summary:	ROX-Filer's base-package
Summary(pl.UTF-8):	Podstawowy pakiet ROX-Filera
Name:		rox-base
Version:	1.0.2
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{name}-%{version}.tgz
# Source0-md5:	46de53c01c6ccea7f3467ce7e37717cc
URL:		http://rox.sourceforge.net/
PreReq:		sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base package needed to run ROX-Filer.

%description -l pl.UTF-8
Pakiet konieczny do uruchomienia ROX-Filera.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/Choices/{MIME-info,MIME-types,MIME-icons} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/rox

install Choices/MIME-icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/Choices/MIME-icons
ln -s %{_datadir}/Choices/MIME-icons $RPM_BUILD_ROOT%{_pixmapsdir}/rox
install Choices/MIME-info/{Standard,gnome-vfs.mime} \
	$RPM_BUILD_ROOT%{_datadir}/Choices/MIME-info
install Choices/MIME-types/{application_postscript,text} \
	$RPM_BUILD_ROOT%{_datadir}/Choices/MIME-types

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/rox/MIME-icons || rm -rf %{_pixmapsdir}/rox/MIME-icons

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/Choices
%{_datadir}/Choices/MIME-icons
%{_datadir}/Choices/MIME-info
%dir %{_datadir}/Choices/MIME-types
%attr(755,root,root) %{_datadir}/Choices/MIME-types/*
%{_pixmapsdir}/rox
