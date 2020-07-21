# -*- coding: utf-8 -*-

def formatString(text, color, b='negro', t='default'):
    colors = { 
             'gris'       : '0',
             'rojo'       : '1',
             'verde'      : '2',
             'amarillo'   : '3',
             'azul'       : '4',
             'violeta'    : '5',
             'cyan'       : '6',
            'blanco'      : '7',
            }
    style = { 
            'default' : '0',
            'negrita' : '1',
            'simple'  : '2',
            'italic'  : '3',
            'sub'     : '4',
            'blink'   : '5',
            'note'    : '6',
            'invert'  : '7',
            }
    # Vamos a generar el valor del fondo, si corresponde o no.
    if b == 'negro':
        value = '0' 
    else:
        value = '4' + colors[b]

    return '\033[' + style[t] + ';' + value  + ';'  + '3' + colors[color] + 'm' + text + '\033[0m'

