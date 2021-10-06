def file2list(filename):
    file=open(filename,encoding='UTF-8')
    str=file.read()
    lista=str.split('/')
    for element in lista:
        if element == "\n":
            lista.remove(element)
        elif element == "":
            lista.remove(element)
        elif element.isspace():
            lista.remove(element)
    return lista

