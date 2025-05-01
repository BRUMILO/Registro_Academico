class Calificaciones:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota
    
    #Metodo encargado de mostrar las notas
    def ver_nota(self):
        print(f"> Materia: {self.materia} -> Nota: {self.nota}")