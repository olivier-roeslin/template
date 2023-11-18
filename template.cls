\LoadClass[a4paper,12pt]{article} % Classe du document
\setlength{\parindent}{0cm}
%--------------------- Packages ------------------------

\RequirePackage[french]{babel} %Langue du document
\RequirePackage[utf8]{inputenc} %Caractères spéciaux
\RequirePackage[section]{placeins}%Pour placement de section
\RequirePackage[T1]{fontenc} %Quelques lettres qui sont pas inclus dans UTF-8
\RequirePackage{mathtools} %Paquet pour des équations et symboles mathématiques
\RequirePackage{siunitx} %Pour écrire avec la notation scientifique (Ex.: \num{2e+9})
\RequirePackage{float} %Pour placement d'images
\RequirePackage{graphicx} %Paquet pour insérer des images
\RequirePackage[justification=centering]{caption} %Pour les légendes centralisées
\RequirePackage{subcaption}
\RequirePackage{wallpaper}
\RequirePackage{nomencl}
%\makenomenclature
\RequirePackage{fancyhdr}
%\pagestyle{fancy}
%\fancyheadoffset{1cm}
%\setlength{\headheight}{2cm}
\RequirePackage{url}
\RequirePackage[hidelinks]{hyperref}%Paquet pour insérer légendes dans des sous-figures comme Figure 1a, 1b
\RequirePackage[left=2.5cm,right=2.5cm,top=2cm,bottom=3.5cm]{geometry} %Configuration de la page
\usepackage{caption} %liste des figures
\usepackage{hyperref} %référence
%\hypersetup{
%    colorlinks=false, % Désactive les liens en couleur
%    hidelinks,        % Cache les liens
%    linkbordercolor=0 0 0, % Couleur de l'encadrement des liens
%}
\usepackage{csquotes} % utilisation \cite
\usepackage[style=numeric-comp, backref=true, backend=biber, sorting=none]{biblatex}% réf format
\usepackage{pythontex}
\usepackage{titlesec} % sous-sous-sous chapitre "\paragraph{Test}"
\setcounter{secnumdepth}{4}
\titleformat{\paragraph} % format \paragraph{Test}
{\normalfont\normalsize\bfseries}{\theparagraph}{1em}{}
\titlespacing*{\paragraph}
{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\usepackage{amsmath}
\usepackage{adjustbox} % ajuster la taille de l'image
\usepackage{enumitem} % jolie énumération
\newlist{myitemize}{itemize}{1} % réglage énumération
\setlist[myitemize,1]{label=--,left=0.5cm} % Utilisation de tirets comme puces
\usepackage{subcaption} % mettre deux images à côté
\usepackage{array}
\usepackage{graphicx}
\usepackage{wasysym} % accolade
\usepackage{tikz} % accolade
\usetikzlibrary{decorations.pathreplacing,calc,tikzmark}
\usepackage{nicematrix} % accolade
\usepackage{tcolorbox} % accolade
\usepackage{pgfplotstable} % excel
\usepackage[utf8]{inputenc} % UTF8 .csv
\usepackage{filecontents}
\usepackage{xcolor}
\usepackage{multirow} % table convert
\usepackage{colortbl} % table convert
\usepackage{pdfpages}