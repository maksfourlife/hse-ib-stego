echo "=== Injection ==="
python main.py inject -image examples/image.png -container examples/cnt.png -input "Hello, world!" -type text
echo "=== Ejection ==="
python main.py eject -container examples/cnt.png -length 13 -type text
