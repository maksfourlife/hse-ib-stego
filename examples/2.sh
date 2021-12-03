echo "=== Prog compilation ==="
# comment this if you have no gcc installed
gcc examples/prog.c -o examples/prog.exe
echo "=== Injection ==="
python main.py inject -image examples/image.png -container examples/cnt.png -input examples/prog.exe -type file
echo "=== Ejection ==="
python main.py eject -container examples/cnt.png -length 55467 -type file -out examples/prog2.exe
echo "== Ejected program execution ==="
examples/prog2.exe
