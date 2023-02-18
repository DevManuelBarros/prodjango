# -*- coding: utf-8 -*-

from formatString import formatString


messeges =  {'menu-welcome'          : """ 
                                       {}
                                    -------------------------------
                                       {}
                                       {}
                                       {}
                                        """.format(formatString('Bienvenido a Prodjango 1.0v', 'blanco', t='blink'),
                                                   formatString('1. Crear Proyecto Django', 'blanco', t='negrita'),
                                                   formatString('2. Abrir Proyecto Django', 'blanco', t='negrita'),
                                                   formatString('3. Salir', 'rojo', t='negrita')
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
            'open_project'          :"""
                                        Listado de proyecto disponibles para abrir.
                                        Seleccione uno por el número de proyecto.
                                     """,
            }

lines =     {'options'      : formatString('Ingrese la opción deseada -> ', 'blanco', t='negrita'),
              'name_project' : formatString('Ingrese un nombre para el proyecto: -> ', 'blanco', t='negrita'),
              'begin_virtual' : formatString('Estamos generando el entorno virtual', 'blanco', t='negrita'),
              'begin_django'  : formatString('Estamos instalando django, tardara un poquito...', 'blanco', t='negrita'),
              'begin_project' : formatString('Estamos creando el proyecto -->  {}', 'blanco', t='negrita'),
              'input_option'  : formatString('Seleccione un proyecto por su ID (la tecla x para salir)  --> ', 'blanco', t='negrita'),
              'process_finish' : formatString('Se ha completado la creación del proyecto {}, pulse enter para continuar', 'blanco', t='negrita'),
              }

styles = {
            'result' : formatString('{}', 'azul')
        }

msg_error = {'error_option'         : formatString('La opción deseada no corresponde o no se corresponde, presione una tecla y continue', 'rojo', b='blanco', t='blink'),
             'error_project_exists' : formatString('El nombre de proyecto esta en uso, intente otro.\n', 'rojo', b='blanco', t='blink')
            }
