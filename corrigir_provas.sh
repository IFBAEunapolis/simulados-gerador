#!/bin/bash

# Gerar lista de arquivos para scanear
find "$(pwd)/rawscans/" > scan-list.txt

# getimages
auto-multiple-choice getimages \
  --list "$PWD/scan-list.txt" \
  --progression-id analyse \
  --vector-density 250 \
  --copy-to "$PWD/scans" \
  --orientation portrait

# analyze
auto-multiple-choice analyse \
  --no-multiple \
  --tol-marque "0.2,0.2" \
  --prop 0.8 \
  --bw-threshold 0.6 \
  --progression-id analyse \
  --progression 1 \
  --n-procs "0" \
  --data data \
  --projet ./ \
  --cr cr \
  --liste-fichiers scan-list.txt \
  --no-ignore-red

# prepare
auto-multiple-choice prepare \
  --n-copies 3 \
  --with lualatex \
  --filter latex \
  --filtered-source DOC-filtered.tex \
  --progression-id bareme \
  --progression 1 \
  --data data \
  --mode b groups.tex

# note
auto-multiple-choice note \
  --data data \
  --seuil 0.15 \
  --grain 0.5 \
  --arrondi inf \
  --notemax 20 \
  --plafond \
  --notemin "" \
  --postcorrect-student "" \
  --postcorrect-copy "" \
  --progression-id notation \
  --progression 1

# association-auto
auto-multiple-choice association-auto \
  --data data \
  --notes-id "<preassoc>" \
  --liste arquivos/alunos.csv \
  --liste-key id \
  --csv-build-name "(nom|surname) (prenom|name)" \
  --encodage-liste UTF-8 \
  --pre-association

# annote
auto-multiple-choice annote --xmlargs annote.xml

# regroupe
auto-multiple-choice regroupe --xmlargs regroupe.xml

# export
auto-multiple-choice export \
  --data data \
  --module csv \
  --fich-noms arquivos/alunos.csv \
  --o exports/resultados.csv
