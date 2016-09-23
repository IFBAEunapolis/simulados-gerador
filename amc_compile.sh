#!/bin/sh

# Receber pasta por meio de parâmetro do bash, se a pasta não for passada usa então a pasta atual.
if [ -n "$1" ]; then
  FOLDER=$1;
else
  FOLDER=$(pwd);
fi;

NUM_COPIES=0
if command -v auto-multiple-choice >/dev/null 2>&1; then
  # Compilar o documento em latex usando o AMC
  auto-multiple-choice prepare \
    --with pdflatex \
    --mode s \
    --filter latex \
    --filtered-source "$FOLDER/DOC-filtered.tex" \
    --out-sujet "$FOLDER/DOC-sujet.pdf" \
    --out-corrige "$FOLDER/DOC-corrige.pdf" \
    --out-catalog "$FOLDER/DOC-catalog.pdf" \
    --out-calage "$FOLDER/DOC-calage.xy" \
    --n-copies 1 "$FOLDER/groups.tex" \
    --prefix "$FOLDER" \
    --latex-stdout "$FOLDER/groups.tex" \
    "$FOLDER/groups.tex"

  auto-multiple-choice prepare \
    --mode b \
    --prefix "$FOLDER" \
    "$FOLDER/groups.tex" \
    --data "$FOLDER/data"

  auto-multiple-choice meptex \
    --src "$FOLDER/DOC-calage.xy" \
    --data "$FOLDER/data"

  auto-multiple-choice imprime \
    --sujet "$FOLDER/DOC-sujet.pdf" \
    --data "$FOLDER/data/" \
    --methode file \
    --output "$FOLDER/Provas/Prova Enade %e.pdf"
else
  "O AMC (AUTO MULTIPLE CHOICE) NÃO ESTÁ INSTALADO. NÃO É POSSIVEL CONTINUAR";
fi;
