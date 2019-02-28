#!/bin/bash

clear

# Replacing all the thymine by uracil
# and put the content in a new file
FILE="rosalind_rna.txt"
OUTPUT="rosalind_output_rna.txt"

sed 's/T/U/g' $FILE > $OUTPUT

# and cat the output file
cat $OUTPUT
