# TODO: optflags

%include	/usr/lib/rpm/macros.java

Summary:	Paintown - an open source fighting game in the same genre as Streets of Rage and Teenage Mutant Ninja Turtles
Summary(hu.UTF-8):	Paintown - egy nyílt forrású verekedős játék a Streets of Rage és a Teenage Mutant Ninja Turtles nyomdokain
Summary(pl.UTF-8):	Paintown - gra zręcznościowa podobna do Streets of Rage lub Teenage Mutants inja Turtles
Name:		paintown
Version:	3.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/paintown/%{name}-%{version}.tar.gz
# Source0-md5:	58de3c1cd8aea7e3117ec97f5e169a23
Source1:	move_list.txt
Source2:	%{name}.desktop
Source3:	%{name}-editor
URL:		http://paintown.sourceforge.net
BuildRequires:	allegro-devel >=4.1
BuildRequires:	ant
BuildRequires:	cmake
BuildRequires:	dumb-devel
BuildRequires:	freetype-devel
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	zlib-devel
Requires:	allegro-alsa
Requires:	jpackage-utils
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

%package editor
Summary:	Paintown editor
Group:		X11/Applications/Games
Requires:	jre-X11

%description editor
Paintown editor.

%prep
%setup -q
%{__sed} -i 's@set(CXXFLAGS.*@set(CXXFLAGS="%{rpmcxxflags}")@g' CMakeLists.txt
RPMCXXFLAGS=$(echo %{rpmcxxflags} | sed "s@ \$@@ ; s@\([^ ]*\)@'\1'@g ; s@ @,@g")
%{__sed} -i "s@^cppflags = .*@cppflags = [ ${RPMCXXFLAGS} ]@" SConstruct

%build
install -d build
cd build
%cmake \
	%{?debug:-DCMAKE_VERBOSE_MAKEFILE=1} \
	..

%{__make}

cd ../editor
ant
sed -i '1i#!%{_bindir}/java -jar' editor.jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp build/bin/paintown .
./install.sh -d $RPM_BUILD_ROOT%{_datadir}/%{name} -b $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE1} .
sed -i "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

install editor/editor.jar $RPM_BUILD_ROOT%{_bindir}/%{name}-editor

install -d $RPM_BUILD_ROOT%{_libdir}
install build/lib/*module* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO scripting.txt doc/character.txt move_list.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}-bin
%{_datadir}/%{name}/data
%{_desktopdir}/%{name}.desktop
%{_libdir}/*.so

%files editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-editor
