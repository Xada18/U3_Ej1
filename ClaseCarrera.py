

class Carrera:
    __codigo = ""
    __nombre = ""
    __titulo = ""
    __duracion = ""
    __fechainicio = ""

    def __init__(self, codigo, nombre, titulo, duracion, fecha):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__fechainicio = fecha

    def __str__(self):
        return self.__codigo + self.__nombre + self.__titulo + self.__duracion + self.__fechainicio


    def getCodigo(cls):
        return cls.__codigo
    
    def getNombre(cls):
        return cls.__nombre
    
    def getTitulo(cls):
        return cls.__titulo
    
    def getDuracion(cls):
        return cls.__duracion
    
    def getFechaInicio(cls):
        return cls.__fechainicio