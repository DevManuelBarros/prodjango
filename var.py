# -*- coding: utf-8 -*-

from formatString import formatString


messeges =  {'menu-welcome'          : """ 
                                       {}
                                    -------------------------------
                                       {}
                                       {}
                                       {}
                                        """.format(formatString('Bienvenido a Prodjango 1.0v', 'rojo', b='blanco', t='blink'),
                                                   formatString('1. Crear Proyecto Django', 'amarillo'),
                                                   formatString('2. Abrir Proyecto Django', 'azul'),
                                                   formatString('3. Salir', 'rojo')
                                                   ),
            
            'exit'                  : """
                                        {} {}
                                        Sugerencias, insultos, agradecimientos a:
                                        
                                        email: {}

                                        Presione una tecla y terminaremos...
                                      """.format(formatString('Gracias por Utilizar:' , 'azul'),
                                                 formatString('Prodjango 1.0v', 'rojo'),
                                                 formatString('dev.manuel.barros@gmail.com', 'rojo')
                                                ),
            }

lines =     {'options'      : formatString('Ingrese la opción deseada -> ', 'blanco', b='violeta'),
              'name_project' : formatString('Ingrese un nombre para el proyecto: -> ', 'blanco', b='violeta'),
              'begin_virtual' : formatString('Estamos generando el entorno virtual', 'verde', b='blanco'),
              'begin_django'  : formatString('Estamos instalando django, tardara un poquito...', 'verde', b='blanco'),
              'begin_project' : formatString('Estamos creando el proyecto -->  {}', 'verde', b='blanco')
              }

msg_error = {'error_option'         : formatString('La opción deseada no corresponde o no se corresponde, presione una tecla y continue', 'rojo', b='blanco', t='blink'),
             'error_project_exists' : formatString('El nombre de proyecto esta en uso, intente otro.\n', 'rojo', b='blanco', t='blink')
            }
