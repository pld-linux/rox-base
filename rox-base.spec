Summary:	ROX-Filer's base-package
Summary(pl):	Podstawowy pakiet ROX-Filera
Name:		rox-base
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{name}-%{version}.tgz
URL:		http://rox.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Base package needed to run ROX-Filer.

%description -l pl
Pakiet konieczny do uruchomienia ROX-Filera.

%prep -q
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/Choices/{MIME-icons,MIME-info,MIME-types}

install Choices/MIME-icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/Choices/MIME-icons
install Choices/MIME-info/{Standard,gnome-vfs.mime} \
	$RPM_BUILD_ROOT%{_datadir}/Choices/MIME-info
install Choices/MIME-types/{application_postscript,text} \
	$RPM_BUILD_ROOT%{_datadir}/Choices/MIME-types

gzip -9nf README
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/Choices/MIME-icons/*
%{_datadir}/Choices/MIME-info/*
%attr(755,root,root) %{_datadir}/Choices/MIME-types/*
%doc README.gz
