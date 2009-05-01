# TODO: optflags
Summary:	Paintown - an open source fighting game in the same genre as Streets of Rage and Teenage Mutant Ninja Turtles
Summary(hu.UTF-8):	Paintown - egy nyílt forrású verekedős játék a Streets of Rage és a Teenage Mutant Ninja Turtles nyomdokain
Summary(pl.UTF-8):	Paintown - gra zręcznościowa podobna do Streets of Rage lub Teenage Mutants inja Turtles
Name:		paintown
Version:	3.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/paintown/%{name}-%{version}.tar.gz
# Source0-md5:	f4c323e3fa6f2a9065923fe40b559be3
Patch0:		%{name}-keyboard-fix.patch
Patch1:		%{name}-stdio.patch
Patch2:		%{name}-verbose-makefile.patch
URL:		http://paintown.sourceforge.net
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

%description -l hu.UTF-8
Paintown - egy nyílt forrású verekedős játék a Streets of Rage és a
Teenage Mutant Ninja Turtles nyomdokain.

%description -l pl.UTF-8
Paintown jest grą zręcznościową tego samego typu co Street of Rage lub
Teenage Mutant Ninja Turtles.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{__sed} -i 's@set(CXXFLAGS.*@set(CXXFLAGS="%{rpmcxxflags}")@g' CMakeLists.txt
RPMCXXFLAGS=$(echo %{rpmcxxflags} | sed "s@ \$@@ ; s@\([^ ]*\)@'\1'@g ; s@ @,@g")
%{__sed} -i "s@^cppflags = .*@cppflags = [ ${RPMCXXFLAGS} ]@" SConstruct

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
