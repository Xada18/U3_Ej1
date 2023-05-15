from ClaseFacultad import Facultad
import csv


class ManejaFacultades:
    __facultades= None

    def __init__(self):
        self.__facultades = []

    def cargaFacultades(self, file):
        archivo = open(file,"r")
        reader = csv.reader(archivo, delimiter=",")

        fcodigo = "a"
        i = -1

        for line in reader:

            if fcodigo == line[0]:
                
                ccodigo = line[1]
                cnombre = line[2]
                titulo = line[3]
                duracion = line[4]
                fecha = line[5]

                self.__facultades[i].crearCarrera(ccodigo, cnombre, titulo, duracion, fecha)
                
            else:

                fcodigo = line[0]
                fnombre = line[1]
                direccion = line[2]
                localidad = line[3]
                telefono = line[4]
                
                facultad = Facultad(fcodigo, fnombre, direccion, localidad, telefono)
                self.__facultades.append(facultad)
                i += 1
                
    
    def mostrarFacultades(self):
        for facultad in self.__facultades:
            print(facultad)
            carreras = facultad.getCarrera()
            for carrera in carreras:
                print(carrera)


               
if __name__ == '__main__':
    archivo = "Facultades.csv"
    listaFacultades = ManejaFacultades()
    listaFacultades.cargaFacultades(archivo)
    listaFacultades.mostrarFacultades()
    


            


