Summary:	ROX-Filer's base-package
Summary(pl):	Podstawowy pakiet ROX-Filera
Name:		rox-base
Version:	1.0.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{name}-%{version}.tgz
URL:		http://rox.sourceforge.net/
Prereq:		sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Base package needed to run ROX-Filer.

%description -l pl
Pakiet konieczny do uruchomienia ROX-Filera.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/Choices/{MIME-info,MIME-types} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/rox/MIME-icons

install Choices/MIME-icons/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/rox/MIME-icons
ln -s %{_pixmapsdir}/rox/MIME-icons $RPM_BUILD_ROOT%{_datadir}/Choices
install Choices/MIME-info/{Standard,gnome-vfs.mime} \
	$RPM_BUILD_ROOT%{_datadir}/Choices/MIME-info
install Choices/MIME-types/{application_postscript,text} \
	$RPM_BUILD_ROOT%{_datadir}/Choices/MIME-types

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_datadir}/Choices/MIME-icons || rm -rf %{_datadir}/Choices/MIME-icons

%files
%defattr(644,root,root,755)
%doc README.gz
%dir %{_datadir}/Choices
%{_datadir}/Choices/MIME-icons
%{_datadir}/Choices/MIME-info
%dir %{_datadir}/Choices/MIME-types
%attr(755,root,root) %{_datadir}/Choices/MIME-types/*
%{_pixmapsdir}/rox
