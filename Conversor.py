#!/usr/bin/env python3

from PIL import Image
import sys
import os
from datetime import datetime
from pdf2image import convert_from_path
import subprocess

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
    imagenes = convert_from_path(parametro, fmt=formato)
    
    print("Iniciando...")
    nombre_carpeta = parametro[:-4]
    os.mkdir(nombre_carpeta)
    os.chdir(nombre_carpeta)

    try:
        paginas = len(imagenes)    
        for i, imagen in enumerate(imagenes):
            nombre_imagen = f"pagina_{i + 1}.{formato}"
            imagen.save(nombre_imagen, formato.upper())
            print(f"\rProcesando pagina {i + 1}/{paginas}", end="")
        print("\nPreceso terminado")

    except Exception as e:
        print(f"Error: {e}")


def world_excel_a_pdf(parametro):
    if ".docx" or ".xlsx" in parametro:
        comando = [
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            parametro
        ]
        subprocess.run(comando, check=True)
        
        print("Proceso terminado con exito")
    else:
        print("Error")
    
def pdf_a_world_excel(parametro):
    print("""A que formato quieres convertir?:
          1.-word 2.-excel""")
    
    elegir = int(input("Elige una opcion: "))

    if ".pdf" in parametro:
        if elegir == 1:
            comando =[
                "libreoffice",
                "--headless",
                "--convert-to", "docx",
                parametro
            ]

            subprocess.run(comando, check=True)

            print("Preceso terminado")

        elif elegir == 2:
            comando = [
                "libreoffice",
                "--headless",
                "--convert-to", "xlsx",
                parametro
            ]        

            subprocess.run(comando, check=True)

            print("Proceso terminado")


print("""Ingresa a que tipo de archivo quieres convertir:
        1.- Una imagen a otro formato 2.- PDF a imagenes 3.-word, excel a pdf""")

eleccion = int(input("Elige el procedimiento: "))

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

elif eleccion == 3:
    world_excel_a_pdf(parametro)
