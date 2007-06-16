Summary:	Eclipse Compiler for Java
Name:		eclipse-ecj
Version:	3.2.2
Release:	0.1
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://distro.ibiblio.org:/pub/linux/distributions/gentoo/distfiles/eclipse-ecj-3.2.2.tar.bz2
# Source0-md5:	21f55de66c2deec51b6714b607b6793f
Patch0:		%{name}-gentoo.patch
URL:		http://www.eclipse.org/
BuildRequires:	ant >= 1.6.1
BuildRequires:	jdk >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildRequires:	zip
Requires:	ant
Requires:	jdk >= 1.4
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86\\|athlon\\|pentium/x86/;s/amd64/x86_64/')
%define		no_install_post_chrpath		1

%description
Eclipse Compiler for Java.

%prep
%setup -q
%patch0 -p1

%build
unset CLASSPATH || :
export JAVA_HOME=%{java_home}

ant -f compilejdtcorewithjavac.xml
ant -lib ecj.jar -f compilejdtcore.xml compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_bindir},%{_libdir}/%{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eclipse
%attr(755,root,root) %{_libdir}/%{name}/eclipse
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%{_desktopdir}/eclipse.desktop
%{_pixmapsdir}/eclipse-icon.xpm
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/.eclipseproduct
%{_libdir}/%{name}/configuration
%{_libdir}/%{name}/eclipse.ini
