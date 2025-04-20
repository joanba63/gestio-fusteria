#!/bin/bash

# Script per fer add, commit i push automàtic
cd "$(dirname "$0")"

# Missatge automàtic amb data/hora
MISSATGE="Auto-commit: $(date '+%Y-%m-%d %H:%M:%S')"

git add .
git commit -m "$MISSATGE"
git push
