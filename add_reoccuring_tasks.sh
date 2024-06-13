#!/bin/bash
cd "$(dirname "$0")"
cd ../todo.txt
cat todo.txt > sorted.all
cat eqt.todo.txt > sorted.eqt
python3 ../igor/art -n > art.txt
grep "EQT" art.txt >> sorted.eqt
grep -v "EQT" art.txt >> sorted.all
sort sorted.all | uniq > todo.txt
sort sorted.eqt | uniq > eqt.todo.txt
rm sorted.all 
rm sorted.eqt
rm art.txt

# This is ugly. It's got to import a bunch of different files and then write to them. That's NOT all that hard but MAYBE  it should be in the python the whole time.


