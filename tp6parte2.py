class Alumno:

    def inicio(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("nombre: ",self.nombre)
        print("nota:  ",self.nota)

    def promedio(self):
        if self.nota < 7:
            print("El alumno ha desaprobado")
        else:
            print("El alumno ha aprobado")

alumnoA = Alumno()
alumnoB = Alumno()
alumnoA.inicio("Matias", 3)
alumnoB.inicio("Andrea", 8)
alumnoA.imprimir()
alumnoA.promedio()
alumnoB.imprimir()
alumnoB.promedio()