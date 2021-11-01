import docx
from modules.functions import *
import os
import re
from modules.IOFunctions import *
todo_filename='toDo.txt'
filename='labs.docx'


def images_section(tuple,group,doc,filename):
    '''
    This function will add a single image according to the instrucction
    :param tuple:tuple of all images 
    :param group: group of images
    :param doc: the instance of the python-docx
    :param filename: document file name


    '''
    for key in group:
        value=tuple[int(key)-1][1]

        imagename=str(key)+" "+str(value)+".png"


        add_image(doc, imagename)
        write(doc, "ch", str(value), filename)

def build_word(filename,todo_filename):
    '''
    This function will put it all together
    :param filename:writes all in the docxs file name
    :param todo_filename: list of instructions to do
   
    '''
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

build_word(filename, todo_filename)
