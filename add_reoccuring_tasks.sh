#!/bin/bash
cd "$(dirname "$0")"
cd ../todo.txt
cat todo.txt > sorted.all
python3 ../igor/art -n > art.txt
cat  art.txt >> sorted.all
sort sorted.all | uniq > todo.txt
rm sorted.all 
rm art.txt

# This is ugly. It's got to import a bunch of different files and then write to them. That's NOT all that hard but MAYBE  it should be in the python the whole time.


