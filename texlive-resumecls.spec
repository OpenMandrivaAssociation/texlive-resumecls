Name:		texlive-resumecls
Version:	0.3.2
Release:	1
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
%{_texmfdistdir}/tex/xelatex/resumecls
%doc %{_texmfdistdir}/doc/xelatex/resumecls
#- source
%doc %{_texmfdistdir}/source/xelatex/resumecls

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
