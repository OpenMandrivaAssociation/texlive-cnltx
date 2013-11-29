# revision 32212
# category Package
# catalog-ctan /macros/latex/contrib/cnltx
# catalog-date 2013-11-22 18:02:28 +0100
# catalog-license lppl1.3
# catalog-version 0.9
Name:		texlive-cnltx
Version:	0.90
Release:	1
Summary:	LaTeX tools and documenting facilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cnltx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cnltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cnltx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a versatile bundle of packages and classes for
consistent formatting of control sequences, package options,
source code examples, and writing a package manual (including
an index containing the explained control sequences, options,
ldots). The bundle also provides several other small ideas of
mine such as a mechansim for providing abbreviations etc. Not
at least it provides a number of programming tools. The
intention behind this bundle mainly is a selfish one:
documenting my own packages. The bundle contains an index style
file cnltx.ist that should be placed in a directory in a TDS
makeindex directory.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/cnltx/cnltx.bib
%{_texmfdistdir}/makeindex/cnltx/cnltx.ist
%{_texmfdistdir}/tex/latex/cnltx/cnltx-base.sty
%{_texmfdistdir}/tex/latex/cnltx/cnltx-doc.cls
%{_texmfdistdir}/tex/latex/cnltx/cnltx-example.sty
%{_texmfdistdir}/tex/latex/cnltx/cnltx-listings.sty
%{_texmfdistdir}/tex/latex/cnltx/cnltx-tools.sty
%{_texmfdistdir}/tex/latex/cnltx/cnltx.bbx
%{_texmfdistdir}/tex/latex/cnltx/cnltx.cbx
%{_texmfdistdir}/tex/latex/cnltx/cnltx.dbx
%{_texmfdistdir}/tex/latex/cnltx/cnltx.sty
%doc %{_texmfdistdir}/doc/latex/cnltx/README
%doc %{_texmfdistdir}/doc/latex/cnltx/cnltx_en.pdf
%doc %{_texmfdistdir}/doc/latex/cnltx/cnltx_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc %{buildroot}%{_texmfdistdir}
