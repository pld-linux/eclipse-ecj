%include	/usr/lib/rpm/macros.java
Summary:	Eclipse Compiler for Java
Summary(pl.UTF-8):	Kompilator Eclipse dla Javy
Name:		eclipse-ecj
Version:	3.2.2
Release:	0.1
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://distro.ibiblio.org/pub/linux/distributions/gentoo/distfiles/%{name}-%{version}.tar.bz2
# Source0-md5:	21f55de66c2deec51b6714b607b6793f
Patch0:		%{name}-gentoo.patch
Patch1:		%{name}-gccmain.patch
URL:		http://www.eclipse.org/
BuildRequires:	ant >= 1.6.1
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	pkgconfig
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildRequires:	zip
Requires:	ant
Requires:	jdk >= 1.4
Requires:	jpackage-utils
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86\\|athlon\\|pentium/x86/;s/amd64/x86_64/')
%define		no_install_post_chrpath		1

%description
Eclipse Compiler for Java.

%description -l pl.UTF-8
Kompilator Eclipse dla Javy.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%ant -f compilejdtcorewithjavac.xml

export CLASSPATH=$PWD/ecj.jar
%ant -lib ecj.jar -f compilejdtcore.xml compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/ecj
#!/bin/sh
. %{_javadir}-utils/java-functions
set_javacmd

CLASSPATH=%{_javadir}/ecj.jar${CLASSPATH:+:}$CLASSPATH \
java org.eclipse.jdt.internal.compiler.batch.Main "$@"
EOF

install ecj.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecj
%{_javadir}/*.jar
