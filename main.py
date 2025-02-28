from PIL import Image
import sys
import os
from datetime import datetime
from pdf2image import convert_from_path

print("Conversor De Archivos".center(50,"*"))

if len(sys.argv) !=2:
    print("Ejemplo de como se usa: \n\tconversor.py image.jpg")
    exit()

parametro = sys.argv[1]

def imagen_a_otro_formato(opcion, formato, imagen):

    formato_selecionado = formato[opcion].lower()
    nuevo_nombre = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.{formato_selecionado}"
    imagen.save(nuevo_nombre, formato_selecionado)
    return nuevo_nombre

def pdf_a_imagenes(parametro, formato="png"):

    carpeta_salida = os.getcwd()

    imagenes = convert_from_path(parametro, fmt=formato)
    for i, imagen in enumerate(imagenes):
        nombre_imagen = f"pagina_(i + 1).{formato}"
        imagen.save(nombre_imagen, formato.upper())
    return print("correcto")

print("""Ingresa a que tipo de archivo quieres convertir:
        1.- Una imagen a otro formato 2.- PDF a imagenes""")

eleccion = int(input("Eleige el procedimiento: "))

if eleccion == 1:

    imagen = Image.open(parametro)

    print("""Elige el formato de imagen a la que quieres convertir
            1.- JPEG 2.- PNG 3.- BMP 4.- TIFF""")
    opcion = input("Elige el formato: ")

    formato = {
        "1": "JPEG",
        "2": "PNG",
        "3": "BMP",
        "4": "TIFF",
    }

    if opcion not in formato:
        print("Opcion no disponible")
        exit()

    imagen_a_otro_formato(opcion, formato, imagen)
    print("Fin")

elif eleccion == 2:

    pdf_a_imagenes(parametro, formato="png")
    
