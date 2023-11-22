#!/bin/bash
cd "$(dirname "$0")"
cd ../todo.txt
cat todo.txt > sorted.all
cat eqt.todo.txt > sorted.eqt
../igor/igor -n > igor.txt
grep "EQT" igor.txt >> sorted.eqt
grep -v "EQT" igor.txt >> sorted.all
# Vision section
#python3 ../vision/vision.py -d > vision.txt
#grep "EQT" vision.txt >> sorted.eqt
#grep -v "EQT" vision.txt >> sorted.all
#rm vision.txt
# End vision section
mv sorted.all todo.txt
mv sorted.eqt eqt.todo.txt
rm igor.txt
