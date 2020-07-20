import os
from var import lines, msg_error
from objSqlite import objSqlite
from datetime import datetime

class project():
    
    __database = ''

    __term = 'env'
    __path_projects = 'prodjango/'
    __name_project = ''
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

    __table_projects = 'projects'
    __table_plugins = 'plugins'
    __hb = '#! bin/bash \n'

    def __create_tables(self):
        self.__create_table(self.__table_projects, self.__projects)
        self.__create_table(self.__table_plugins, self.__plugins)
        return True

    def __create_table(self, table, fields):
        objLite = objSqlite(self.__database)
        tmpCad = ''
        for k, v in fields.items():
            tmpCad += k + ' ' + v + ','
        tProjects = {table : tmpCad[:-1]}
        result =  objLite.create_table(tProjects)
        objLite.close()
        return result

    def whichPy(self, program):
        if os.system('which {} > /dev/null'.format(program))==0:
            return True
        else:
            return False


    def create_init_install(self):
        env = 'virtualenv'
        if(self.whichPy(env)==False):
            print('actualizaremos sistema...')
            os.system('sudo apt-get update > /dev/null')
            os.system('sudo apt-get install {} > /dev/null'.format(env))
        #haremos una ruta.
        print(lines['begin_virtual'])
        rel_path = self.__path_projects + self.__name_project
        exe = '{} {}/{}{} > /dev/null'.format(env, rel_path, self.__name_project, self.__term)
        os.system(exe)
        code = self.__hb + '. {}{}/{}{}/bin/activate > /dev/null'.format(self.__path_projects,
                                                self.__name_project,
                                                self.__name_project,
                                                self.__term)
        code += '\npip install django > /dev/null'
        code += '\ndjango-admin startproject {} {}/'.format(self.__name_project,                                                            rel_path)
        print(lines['begin_django'])
        os.system(code)


    def create_project(self, name_project):
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



    def __prepare_dict_projects(self):
        tmpDict = self.__projects.copy()
        tmpDict.pop('id')
        return tmpDict

    def __comp_path(self, _dir):
        #_dir = os.path.abspath(os.path.join(_dir))
        if ~(os.path.isdir(_dir)):
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

            
