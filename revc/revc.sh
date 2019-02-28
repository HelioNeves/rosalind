#!/bin/bash

clear

# Replacing order: 
# T -> X | A -> T | X -> A
# C -> X | G -> C | X -> G
# X as a auxiliary variable
# and using rev to revert the output
FILE="rosalind_revc.txt"
OUTPUT="rosalind_revc_output.txt"

sed 's/T/X/g
     s/A/T/g
     s/X/A/g
     s/C/X/g
     s/G/C/g
     s/X/G/g' $FILE | rev > $OUTPUT

# and cat the output file
cat $OUTPUT
