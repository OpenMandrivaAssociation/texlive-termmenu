Name:		texlive-termmenu
Version:	37700
Release:	1
Summary:	The package provides support for terminal-based menus using expl3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/termmenu
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termmenu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termmenu.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termmenu.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
When writing programs, it's often required to present the user
with a list of options/actions. The user is then expected to
select one of these options for the program to process.
termmenu provides this mechanism for TeX. It requires only
expl3 support, thus the l3kernel and l3packages are both
required.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/termmenu
%{_texmfdistdir}/tex/generic/termmenu
%doc %{_texmfdistdir}/doc/generic/termmenu

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
