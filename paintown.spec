Summary:	Paintown is an open source fighting game in the same genre as Streets of Rage and Teenage Mutant Ninja Turtles
Summary(pl.UTF-8):	Paintown jest grą zręcznościową podobną do Streets of Rage lub Teenage Mutants inja Turtles
Name:		paintown
Version:	3.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/paintown/%{name}-%{version}.tar.gz
# Source0-md5:	0b5c5113022d92e76f0e19d4aa523e29
URL:		http://paintown.sourceforge.net
Patch0:		%{name}-keyboard-fix.patch
BuildRequires:	allegro-devel >=4.1
BuildRequires:	cmake
BuildRequires:	dumb-devel
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Paintown is an open source fighting game in the same genre as Streets
of Rage and Teenage Mutant Ninja Turtles.

%description -l pl.UTF-8
Paintown jest grą zręcznościową tego samego typu co Street of Rage
lub Teenage Mutant Ninja Turtles.

%prep
%setup -q
%patch0 -p1

%build
mkdir build
cd build
cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cp build/bin/paintown .
install -d $RPM_BUILD_ROOT%{_bindir}
./install.sh -d $RPM_BUILD_ROOT%{_datadir}/%{name} -b $RPM_BUILD_ROOT%{_bindir}
sed -i "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/%{name}-bin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
