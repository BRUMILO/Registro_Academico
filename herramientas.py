from estudiante import Estudiante

#Lista goblal de datos de estudiante
estudiantes = []

#Funcion que registra los datos del estudiante
def registrar_estudiante():
    print("\n\t| Registrar Estudiante |\n")
    nombre = input("- Ingrese el nombre del estudiante: ")
    matricula = input("- Ingrese el Nro matricula: ")
    carrera = input("- Ingrese la carrera: ")
    
    estudiantes.append(Estudiante(nombre, matricula, carrera))
    
#Funcion que se encarga de buscar al estudiante por nro de matricula en la lista "estudiantes"
def buscar_estudiante(matricula):
    for i in range(len(estudiantes)):
        if estudiantes[i].matricula == matricula:
            return i
    return None

#Funcion encargada de asignar las notas a cada estudiante 
def asignar_notas_materia():
    if estudiantes != []:
        print("\n\t| Registrar Notas |\n")
        pos_estudiante = ingresar_matricula()

        while True:
            materia = input("- Ingrese el nombre de la materia: ")

            while True:
                try:
                    nota = int(input("- Ingrese la nota: "))
                    if nota < 0 or nota > 50:
                        print("| Valor no válido |")    
                    else:
                        break            
                except ValueError:
                    print("| Valor no válido |")
                    
            estudiantes[pos_estudiante].ingresar_notas(materia, nota)
            
            if input("> Desea ingresar otro estudiante?:\n(1) Si\n(2) No\n> Seleccione: ") == "2":
                break
            
    else:
        print("\n| No existen estudiantes registrados, porfavor registre uno |\n")        
    
#Funcion encargada de mostrar a un estudiante en especifico
def ver_estudiante():
    if estudiantes != []:
        print("\n\t| Ver Estudiante |\n")
        pos_estudiante = ingresar_matricula()
        
        estudiantes[pos_estudiante].visualizar_datos(mostrar_notas = True)
            
    else:
        print("\n| No existen estudiantes registrados, porfavor registre uno |\n")
        
#Funcion encargada de buscar la posicion del estudiante en la lista y retornar su posicion
def ingresar_matricula():
    while True:
        matricula = input("> Ingrese el Nro de matricula del estudiante: ")
        pos_estudiante = buscar_estudiante(matricula)
        if pos_estudiante != None:
            return pos_estudiante        
        else:
            print("| Estudiante no registrado |")

#Funcion encargada de mostrar todos los estudiantes registrados en la lista
def mostrar_estudiantes():
    if estudiantes != []:
        for i in estudiantes:
            i.visualizar_datos()            
    else:
        print("\n| No existen estudiantes registrados, porfavor registre uno |\n")                                         