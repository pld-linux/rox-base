Summary:	ROX-Filer's base-package
Summary(pl):	Podstawowy pakiet ROX-Filer'a
Name:		rox-base
Version:	1.0.0
Release:	1
License:	GPL (?)
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	%{name}-%{version}.tgz
BuildRequires:	automake autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Base package needed to run ROX-Filer

%description -l pl
Pakiet konieczny do uruchomienia ROX-Filer'a

%prep -q
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/Choices/{MIME-icons,MIME-info,MIME-types}

install Choices/MIME-icons/* $RPM_BUILD_ROOT%{_datadir}/Choices/MIME-icons
install Choices/MIME-info/* $RPM_BUILD_ROOT%{_datadir}/Choices/MIME-info
install Choices/MIME-types/* $RPM_BUILD_ROOT%{_datadir}/Choices/MIME-types

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/Choices/MIME-icons
%{_datadir}/Choices/MIME-info
%attr(755,root,root) %{_datadir}/Choices/MIME-types
