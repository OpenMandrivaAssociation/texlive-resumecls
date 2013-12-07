# revision 29417
# category Package
# catalog-ctan /macros/xetex/latex/resumecls
# catalog-date 2013-03-17 10:58:10 +0100
# catalog-license lppl1.3
# catalog-version 0.2.1
Name:		texlive-resumecls
Version:	0.2.1
Release:	2
Summary:	Typeset a resumee in both Chinese and English
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/resumecls
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumecls.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumecls.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumecls.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides a simple resumee structure that works,
natively, with both Chinese and English text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/resumecls/resumecls.cls
%doc %{_texmfdistdir}/doc/xelatex/resumecls/Makefile
%doc %{_texmfdistdir}/doc/xelatex/resumecls/README
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/Makefile
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/README.md
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/config-sample.mk
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/config.mk
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/resume-en.pdf
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/resume-en.tex
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/resume-zh.pdf
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/resume-zh.tex
%doc %{_texmfdistdir}/doc/xelatex/resumecls/example/resume.bib
%doc %{_texmfdistdir}/doc/xelatex/resumecls/resumecls.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/resumecls/resumecls.dtx
%doc %{_texmfdistdir}/source/xelatex/resumecls/resumecls.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
