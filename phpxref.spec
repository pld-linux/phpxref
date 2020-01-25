Summary:	PHP Cross Referencing Documentation Generator
Summary(pl.UTF-8):	Generator dokumentacji z odwołaniami do kodu w PHP
Name:		phpxref
Version:	0.7
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phpxref/%{name}-%{version}.tar.gz
# Source0-md5:	9518c12578c6daa6ee69bd23379ec8ba
Patch0:		%{name}-javascriptfix.patch
URL:		http://phpxref.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-base >= 1:5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
PHPXref is a developer tool that's designed to ease the process of
working on large PHP projects by making it very fast and easy to
browse the code documentation along with the code itself.

%description -l pl.UTF-8
PHPXref to narzędzie programistyczne zaprojektowane w celu ułatwienia
pracy z dużymi projektami w PHP poprzez szybkie i łatwe przeglądanie
dokumentacji do kodu wraz z samym kodem.

%prep
%setup -q
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
install phpxref.pl $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a phpxref.cfg $RPM_BUILD_ROOT%{_appdir}
cp -a jstree *.js *.gif php4_functionlist.txt $RPM_BUILD_ROOT%{_appdir}
cp -a sample* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog UPGRADE README.html
%attr(755,root,root) %{_bindir}/phpxref
%{_appdir}
