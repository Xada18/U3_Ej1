from ClaseCarrera import Carrera


class Facultad:
    __codigo = ""
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carrera=None

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carrera = []
    
    def crearCarrera(self, codigo, nombre, fecha, duracion, titulo):
        carrera = Carrera(codigo, nombre, fecha, duracion, titulo)
        self.__carrera.append(carrera)


    def getCarrera(self):
        return self.__carrera

    def __str__(self):
        return self.__codigo + self.__nombre + self.__direccion + self.__localidad + self.__telefono 

