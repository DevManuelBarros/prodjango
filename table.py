import os


class table:

    columns = 0
    __maxWidth = 1
    __headers = 0
    __charLineVertical = '|'
    __charLineHorizontal = '-'
    
    __dictAlign = {
                    'center' : '^',
                    'left'   : '<',
                    'right'  : '>',
                 } 


    __headers = ''
    __body    = ''

    def __init__(self, columns):
        ''' al inicar se debe declarar la cantidad de columnas.'''
        self.columns = columns


    def setMaxWidth(self, _max):
        ''' Permite setear el maximo de ancho que tendra la tabla. ''' 
        self.__maxWidth = _max

    def setCharLineVertical(self, char):
        self.__charLineVertical = char

    def setCharLineHorizontal(self, char):
        self.__charLineHorizontal = char

    def __maxString(self, tupla):
        ''' Devuelve el valor de la candena más grande'''
        _max = 0
        for i in tupla:
            if len(i) > _max:
                _max = len(i)
        return _max

    def setHeaders(self, headers, align='center'):
        '''Setea una tupla que contiene los datos '''
        table = []
        align = self.__dictAlign[align]
        if len(headers) != self.columns:
            raise Exception('el ancho de columan declarado debe coincidir con la cabecera.')
        else:
            _max = self.__maxString(headers)
            if _max > self.__maxWidth:
                raise Exception('Hay una cadena que es mayor que el valor Maximo de Ancho. Utilice setMaxWidth')
            title = self.__charLineVertical
            for item in headers:
                title += '{item:{align}{value}s}{line}'.format(item=item,
                                                         align=align,
                                                         value=self.__maxWidth,
                                                         line=self.__charLineVertical)
            title = title
            lineHorizontal = self.__charLineHorizontal * len(title)
            table.append(lineHorizontal)
            table.append(title)
            table.append(lineHorizontal)
        self.__headers =  table


    def __classType(self, item):
        align = '^'
        t     = 's'
        max_with = self.__maxWidth
        item = item
        if isinstance(item, bool):
            item = str(item)
        elif isinstance(item, float):
            max_with = str(max_with) + '.2'
            t = 'f'
            align = '>'
        elif isinstance(item, int):
            t = 'd'
            align = '>'
        elif isinstance(item, str):
            align = '<'
        
        return align, t, max_with, item


    def setBody(self, data):
        ''' Realizamos un seteo de los datos '''
        table = []
        for reg in data:
            data = self.__charLineVertical
            for item in reg:
                align, tType, max_with, item = self.__classType(item)            
                data += '{item:{align}{value}{t}}{line}'.format(item=item,
                                                                align=align,
                                                                value=max_with,
                                                                t=tType,
                                                                line=self.__charLineVertical)
            line = self.__charLineHorizontal * len(data)
            table.append(data)
            table.append(line)
        self.__body = table

    def print_table(self):
        ''' Imprime la tabla '''
        for i in self.__headers:
            print(i)
        for i in self.__body:
            print(i)


