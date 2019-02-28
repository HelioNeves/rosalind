#!/bin/bash

clear

# Listing the ocurrences with grep 
# and count such lines with word count
A="$(grep 'A' -o rosalind_dna.txt | wc -l)" 
C="$(grep 'C' -o rosalind_dna.txt | wc -l)" 
G="$(grep 'G' -o rosalind_dna.txt | wc -l)" 
T="$(grep 'T' -o rosalind_dna.txt | wc -l)"

# All commands as formatted output
echo "${A} ${C} ${G} ${T}"
