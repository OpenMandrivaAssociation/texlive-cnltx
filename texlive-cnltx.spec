Name:		texlive-cnltx
Version:	55265
Release:	2
Summary:	LaTeX tools and documenting facilities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cnltx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cnltx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cnltx.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bib/cnltx
%{_texmfdistdir}/makeindex/cnltx
%{_texmfdistdir}/tex/latex/cnltx
%doc %{_texmfdistdir}/doc/latex/cnltx

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc %{buildroot}%{_texmfdistdir}
