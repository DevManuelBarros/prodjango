#!/usr/bin/python3
# -*- coding: utf-8 -*-   

import os
from var import messeges, lines, msg_error
from project import project

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


def openProject():
    pass

def main():
    _continue = True
    while(_continue):
        cls()
        print(messeges['menu-welcome'])
        _option = input(lines['options'])
        if _option == '1':
            makeProject()
        elif _option == '2':
            print('ok')
        elif _option == '3':
            _continue = False
            printWait(messeges['exit'])
            cls()
        else:
            printWait(msg_error['error_option'], clean=True)


if __name__ == "__main__":
    main()

