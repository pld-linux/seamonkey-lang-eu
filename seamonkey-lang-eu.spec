Summary:	eu-ES resources for SeaMonkey
Summary(pl):	eu-ES pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-eu
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.eu-ES.langpack.xpi
# Source0-md5:	65ac69003ff53faefc76467dfac8ac51
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
eu-ES resources for SeaMonkey.

%description -l pl
eu-ES pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{ES,eu-ES,eu-unix}.jar > lang-eu-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{ES,eu-ES,eu-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-eu-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/eu-ES.jar
%{_chromedir}/eu-unix.jar
# warning, file conflict with seamonkey-lang-es
%{_chromedir}/ES.jar
%{_chromedir}/lang-eu-installed-chrome.txt
# warning, possible file conflict with seamonkey-lang-es
%{_datadir}/seamonkey/defaults/profile/ES
