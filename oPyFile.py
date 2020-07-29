import os
import json
#import ast

"""
oPyFile.
Es una pequeña clase para manipular los archivos settings.py de Django, 
parsea los datos para que posteriormente pueda manipularse sin problemas

__ini__ carga el nombre del archivo y automaticante llama a readManager.

ReadManager lee linea a linea y tiene los siguientes criterios:
  _newline esta en 0 comienza la primera comparación, 
    si encuenta en la linea un '=', los divide porque encontró una variable.
    por un lado guarda la parte cero que sea la KEY del diccionario, y por el otro comienza a analizar la parte[1]
        realiza una comprobación que no encuentre los valores --> [{ , si los encuentra probablemente tengamos más
        de una linea, entonces comienza a sumar y restar, los parentesis y corchetes tienen valores que se anulan cuando se cierran
        queda en cero y _newline puede terminar, mientras tanto realizan las comprobaciones correspondiente.
"""

class oPyFile:
    
    __oPyDict = {}
    __chars = '[{'
    __path = ''
    __file = ''

    dictValuesKey = {
                        '[' : 1,
                        ']' : -1,
                        '{' : 2,
                        '}' : -2,
                    }

    def __init__(self, path, file_name):
        self.__path = path
        self.__file_name = file_name
        self.readManager()

    def __haveOneValue(self, string, array):
        for i in array:
            if string.__contains__(i):
                return True
        return False

    def __countChars(self, string):
        cont = 0
        for i in string:
            if i in self.dictValuesKey:
                cont += int(self.dictValuesKey[i])
        return cont

    def __clearString(self, string):
        string = string.strip()
        string = string.replace('\n', '')
        return string


    def getDictSetting(self):
        return self.__oPyDict

    def readManager(self):
        #open the file.
        with open(os.path.join(self.__path, self.__file_name), 'rt') as file:
                _newline = 0    #valor para comprobar si podemos recorrer normalmente las lineas. o nos encontramos con un dict o list
                _tmpCad = ''    #si tenemos una list o dict tenemos que ir guardando los valores
                _tmpKey = ''    #igual que tmpCad.
                _cont_import = 1    #Para las importaciones, todas estaran en key 'import'+_cont_import
                #read line to line
                for line in file:
                    if _newline == 0:
                        if line.__contains__('='):
                            part = line.split('=', 1)  # tomamos el primer valor sino tomara varias linea por ejemplo en secret key
                            if self.__haveOneValue(part[1], self.__chars): 
                                #Si entra aqui es porque es una variables que los valores se dividen en varias lineas.
                                _tmpKey = self.__clearString(part[0]) #limpiamos todas las cadenas.
                                _tmpCad = self.__clearString(part[1])
                                _newline = self.__countChars(part[1]) #contamos los valores.
                            else:
                                #si entro acá es una variable simple.
                                self.__oPyDict[part[0]] = self.__clearString(part[1])
                        elif line.__contains__('import'):
                            #entramos en los imports.
                            self.__oPyDict['import{}'.format(_cont_import)] = self.__clearString(line)
                            _cont_import += 1
                    else:
                        #si _newline no es cero, hay que hacer procedimientos
                        _tmpCad += self.__clearString(line)
                        self.__oPyDict[_tmpKey] = _tmpCad
                        _newline += self.__countChars(line)
                        después de hacer la comprobación de caracteres
                        #de ser necesario borramos los valores almacenados
                        if _newline == 0:
                            _tmpKey = ''
                            _tmpCad= ''



