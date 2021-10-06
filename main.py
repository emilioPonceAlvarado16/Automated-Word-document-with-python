import docx
from functions import *
import os
import re
from IOFunctions import *
todo_filename='toDo.txt'
filename='labs.docx'


def images_section(tuple,grupo,doc,filename):
    for key in grupo:
        value=tuple[int(key)-1][1]

        imagename=str(key)+" "+str(value)+".png"


        add_image(doc, imagename)
        write(doc, "ch", str(value), filename)

def hacer_word(filename,todo_filename):
    lista = os.listdir()
    tupla_imagenes = image_tuple_generator(lista)
    doc = docx.Document(filename)
    instrucciones = file2list(todo_filename)

    for instruccion in instrucciones:
        pattern = r"\w*"
        match = re.search(pattern, instruccion)
        if match[0] == "im":  # La primera palabra
            pattern2 = r"[0-9]+"
            match = re.findall(pattern2, instruccion)
            images_section(tupla_imagenes, match, doc,filename)  # enviar las imagenes a subir jeje
        else:

            write(doc, match[0], instruccion[3:], filename)

    doc.save(filename)
    print("Done! ")

hacer_word(filename, todo_filename)