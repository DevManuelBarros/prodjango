import os
from var import lines, msg_error
from objSqlite import objSqlite
from datetime import datetime

class project():
    

    # variables para un proyecto abierto
    __oProject_id   = ''
    __oProject_name = ''
    __oPath_project = ''
    

    # varibales generales
    __database = ''
    
    __term = 'env'                              # terminación de loa entornos virtuales.
    __path_projects = 'prodjango/'              # path del proyecto. posteriormente realizar carpetas independientes.
    __name_project = ''                         # nombre del proyecto cuando se esta creando.
    
    
    # datos de la bases de datos a generar según objSqlite
    __projects  = {                     
                    'id'          : 'ip',
                    'name'        : 'tu',
                    'date_create' : 't',
                    'path'        : 't',
                    'path_env'    : 't', 
                    }
    __plugins = {
                'id'          : 'ip',
                'name'        : 't',
                'id_project'  : 'i',
                'script'      : 't',
                'data_create' : 't',
            }

    # cada diccionario tiene una variable asociada.
    __table_projects = 'projects'
    __table_plugins = 'plugins'
    __hb = '#! bin/bash \n'



    def __create_tables(self):
        ''' Para centralizar la creacion de tablas, llama a la función __create_table '''
        self.__create_table(self.__table_projects, self.__projects)
        self.__create_table(self.__table_plugins, self.__plugins)
        return True

    def __create_table(self, table, fields):
        ''' Función para la creación de tablas en la base datos. '''                
        objLite = objSqlite(self.__database)
        tmpCad = ''
        for k, v in fields.items():
            tmpCad += k + ' ' + v + ','
        tProjects = {table : tmpCad[:-1]}
        result =  objLite.create_table(tProjects)
        objLite.close()
        return result

    def whichPy(self, program):
        ''' pequeño script para ver si existe un proceso. '''
        if os.system('which {} > /dev/null'.format(program))==0:
            return True
        else:
            return False


    def create_init_install(self):
        ''' creamos las instanciones iniciales '''
        # utilizaremos virtualenv para generar el directorio virtual.
        env = 'virtualenv'
        # comprobamos que exista.
        if(self.whichPy(env)==False):                                   # si no existe virtualenv lo instalamos.
            print('actualizaremos sistema...')
            os.system('sudo apt-get update > /dev/null')
            os.system('sudo apt-get install {} > /dev/null'.format(env))
        # haremos una ruta.
        print(lines['begin_virtual'])
        rel_path = self.__path_projects + self.__name_project
        # quedara algo como: virtualenv prodjango/projecto/projectoenv
        exe = f'{env} {rel_path}/{self.__name_project}{self.__term} > /dev/null' #.format(env, rel_path, self.__name_project, self.__term)
        os.system(exe)
        #__hb cabecera del script. code hará es crear un projectos con los datos indicados.
        code = self.__hb + f'. {rel_path}/{self.__name_project}{self.__term}/bin/activate > /dev/null'
        code += '\npip install django > /dev/null'
        code += f'\ndjango-admin startproject {self.__name_project} {rel_path}/'
        print(lines['begin_django']) # avisa que en la proxima linea empieza el script.
        os.system(code)


    def create_project(self, name_project):
        ''' funcion desde donde se puede generar el proyecto. '''
        # Primero comprobamos que no exista el proyecto.
        objLite = objSqlite(self.__database)
        result = objLite.selectWhere(self.__table_projects, cond='name=\'{}\''.format(name_project),columns='id')
        if len(result) > 0:
            return msg_error['error_project_exists']
        else:
            print(lines['begin_project'].format(name_project))
            dictProject = self.__prepare_dict_projects()
            dictProject['name'] = name_project
            dictProject['date_create'] = datetime.now().strftime('%Y-%M-%d')
            dictProject['path'] = str(self.__path_projects + name_project + '/')
            self.__comp_path(dictProject['path'])
            self.__name_project = name_project
            return objLite.insert(self.__table_projects, dictProject)


    def get_list_proyect(self):
        objLite = objSqlite(self.__database)
        result = objLite.selectAll(self.__table_projects, columns='id,name,path')
        return result


    def work_project(self, _id, _name, _path):
        ''' cargamos los datos para abrir el proyecto '''
        self.__oProject_id   = _id
        self.__oPath_project = _path
        self.__oProject_name = _name



    def __prepare_dict_projects(self):
        tmpDict = self.__projects.copy()
        tmpDict.pop('id')
        return tmpDict

    def __comp_path(self, _dir):
        #_dir = os.path.abspath(os.path.join(_dir))
        if not(os.path.isdir(_dir)):
            try:
                os.mkdir(_dir)
            except os.error as e:
                return e
        return str(_dir)



    def __init__(self, database):
        self.__database = database
        if ~(os.path.exists(self.__database)):
            self.__create_tables()
        self.__comp_path(self.__path_projects)    

            
