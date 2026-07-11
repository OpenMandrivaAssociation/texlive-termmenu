%global tl_name termmenu
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The package provides support for terminal-based menus using expl3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/termmenu
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/termmenu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/termmenu.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/termmenu.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
When writing programs, it's often required to present the user with a
list of options/actions. The user is then expected to select one of
these options for the program to process. termmenu provides this
mechanism for TeX. It requires only expl3 support, thus the l3kernel and
l3packages are both required.

