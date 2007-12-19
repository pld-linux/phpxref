%include	/usr/lib/rpm/macros.perl
Summary:	PHP Cross Referencing Documentation Generator
Name:		phpxref
Version:	0.7
Release:	0.1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phpxref/%{name}-%{version}.tar.gz
# Source0-md5:	9518c12578c6daa6ee69bd23379ec8ba
URL:		http://phpxref.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPXref is a developer tool that's designed to ease the process of
working on large PHP projects by making it very fast and easy to
browse the code documentation along with the code itself.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install phpxref.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog UPGRADE
