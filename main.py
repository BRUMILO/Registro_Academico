from herramientas import registrar_estudiante, asignar_notas_materia, ver_estudiante, mostrar_estudiantes

#Funcion principal que controla el Menu
def menu():
    while True:
        
        print("\n\t| Sistema de Registro Academico |\n")
        print("(1) Registrar Estudiante\n(2) Asignar Notas Estudiante\n(3) Ver Estudiante\n(4) Ver Estudiantes\n(5) Salir")
        
        while True:
            try:
                op = int(input("> Ingrese su selección: "))
                break
            except ValueError:
                print("| Opción no válida |")

        match op:
            case 1:
                registrar_estudiante()
                
            case 2:
                asignar_notas_materia()
                
            case 3:
                ver_estudiante()
                
            case 4:
                mostrar_estudiantes()
                
            case 5:
                print("\n>> Programa finalizado <<\n")
                break
                
            case _:
                print("| Opción no válida |")

if __name__ == "__main__":
    menu()