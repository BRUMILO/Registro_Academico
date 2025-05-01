from calificaciones import Calificaciones

class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.notas = []

    #Metodo encargado de asignar la nota de estudiante y guardarlo en un lista
    def ingresar_notas(self, materia, notas):
        self.notas.append(Calificaciones(materia, notas))
    
    #Metodo encargado de mostrar los datos del estuiante
    def visualizar_datos(self, mostrar_notas = False):
        print("\n=================================")
        print(f"> Nombre: {self.nombre}")
        print(f"> Matricula: {self.matricula}")
        print(f"> Carrera: {self.carrera}")
        if mostrar_notas:
            print("----------------------------------")
            for i in self.notas:
                i.ver_nota()        
        print("=================================")