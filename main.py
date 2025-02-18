from PIL import Image
import os
import sys

print("Conversor De Archivos".center(50, "*"))

if len(sys.argv) != 2:
    print("Ejemplo de como se usa: \n\tconversor.py image.jpg")
    exit()

parametro = sys.argv[1]
print(parametro)