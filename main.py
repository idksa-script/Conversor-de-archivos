from PIL import Image
import sys
from datetime import datetime
print("Conversor De Archivos".center(50, "*"))

if len(sys.argv) != 2:
    print("Ejemplo de como se usa: \n\tconversor.py image.jpg")
    exit()

parametro = sys.argv[1]
imagen = Image.open(parametro)

print("""Ingresa a que formato quieres convertir esta imagen:
      1.- JPEG
      2.- PNG
      3.- BMP
      4.- GIF
      5.- TIFF
      6.- WEBP""")

opcion = input("Elige un formato: ")

formato = {
    "1": "JPEG",
    "2": "PNG",
    "3": "BMP",
    "4": "GIF",
    "5": "TIFF",
    "6": "WEBP"
}

if opcion not in formato:
    print("Error: opcion no valida")
    exit()

formato_selecionado = formato[opcion].lower()
nuevo_nombre = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.{formato_selecionado}"
print(nuevo_nombre)