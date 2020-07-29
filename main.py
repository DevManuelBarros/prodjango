#!/usr/bin/python3
# -*- coding: utf-8 -*-   

import os
from var import messeges, lines, msg_error, styles
from project import project
from table import table
#Datos
__sqlite     =  'data.db'



def cls():
    os.system('clear')

def printWait(messege, clean=False):
    print(messege)
    input()
    if clean == True:
        cls()

def makeProject():
    objP  = project(__sqlite)
    name_p = input(lines['name_project'])
    objP.create_project(name_p)
    objP.create_init_install()


def work_project(tupla):
    cls()
    objP = project(__sqlite)
    #tupla esta armado por 0=id, 1=name 2=path
    objP.work_project(tupla[0], tupla[1], tupla[2])
    

def openProject():
    cls()
    print(messeges['open_project'])
    objP = project(__sqlite)
    result = objP.get_list_proyect()
    selectTrue= False
    data_project = ''
    while not(selectTrue):
        headers = ('ID','NOMBRE', 'RUTA')
        tab = table(len(headers))
        tab.setMaxWidth(30)
        tab.setHeaders(headers)
        tab.setBody(result)
        tab.print_table()
        #for i in result:
        #    print(styles['result'].format(i))
        select_project = input(lines['input_option'])
        if select_project.isnumeric():
            select_project = int(select_project)
            for tupla in result:
                if select_project == tupla[0]:
                    selectTrue = True
                    objP = None
                    work_projec(tupla)
        else:
            print('Ingrese un valor valido, un ID')
    
    input('Salio')

def main():
    _continue = True
    while(_continue):
        cls()
        print(messeges['menu-welcome'])
        _option = input(lines['options'])
        if _option == '1':
            makeProject()
        elif _option == '2':
            openProject()
        elif _option == '3':
            _continue = False
            printWait(messeges['exit'])
            cls()
        else:
            printWait(msg_error['error_option'], clean=True)


if __name__ == "__main__":
    main()

