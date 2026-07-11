%global tl_name resumecls
%global tl_revision 54815

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4.1
Release:	%{tl_revision}.1
Summary:	Typeset a resume both in English and Chinese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/resumecls
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/resumecls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/resumecls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/resumecls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX document class to typeset a resume or CV both in English and
Chinese with more ease and flexibility.

