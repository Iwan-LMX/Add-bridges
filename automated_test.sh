#!/bin/bash

# Set the path to your executables
BRIDGEN="./Win/bridgen.exe"
HASHI_PY="python hashi.py"
BRIDGECHECK="./Win/bridgecheck.exe"

# Set the numbers for your tests
number1=10
number2=20

# Step 1: Generate input files with ./bridgen.exe
$BRIDGEN $number1 $number2 > ./TestCases/test_${number1}_${number2}.txt
echo "Generated input file: test_${number1}_${number2}.txt"

# Step 2: Run python script with the generated file as input
cat ./TestCases/test_${number1}_${number2}.txt | $HASHI_PY > ./Outputs/test_${number1}_${number2}_hashi_out.txt
echo "Generated hashi.py output file: test_${number1}_${number2}_hashi_out.txt"

# Step 4: Run ./bridgecheck.exe with specific input and output files
Get-Content ./Outputs/test_${number1}_${number2}_out.txt | $BRIDGECHECK  ./TestCases/test_${number1}_${number2}_in.txt