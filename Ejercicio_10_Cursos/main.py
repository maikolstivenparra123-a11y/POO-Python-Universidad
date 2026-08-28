class Profesor:
    def __init__(self, identificacion: str, nombre: str):
        self.identificacion = identificacion
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Profesor: {self.nombre} (ID: {self.identificacion})"


class Estudiante:
    def __init__(self, identificacion: str, nombre: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.calificaciones = []

    def registrar_calificacion(self, nota: float):
        if 0.0 <= nota <= 5.0:
            self.calificaciones.append(nota)

    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Promedio: {self.calcular_promedio():.2f}"


class Curso:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = None
        self.estudiantes = []

    def asignar_profesor(self, profesor: Profesor):
        self.profesor = profesor

    def matricular_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, identificacion: str):
        for e in self.estudiantes:
            if e.identificacion == identificacion:
                return e
        return None

    def mostrar_informacion(self):
        print(f"\nCurso: {self.nombre} (Código: {self.codigo})")
        prof = self.profesor.nombre if self.profesor else "Sin asignar"
        print(f"Profesor: {prof}")
        print("Estudiantes:")
        if not self.estudiantes:
            print("  Sin estudiantes matriculados.")
        for e in self.estudiantes:
            print(f"  - {e}")


def menu():
    cursos = []
    profesores = []

    while True:
        print("\n1. Crear curso\n2. Registrar profesor\n3. Asignar profesor a curso\n4. Matricular estudiante\n5. Registrar calificación\n6. Calcular promedio de estudiante\n7. Mostrar información de cursos\n8. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cod = input("Código del curso: ").strip()
            nombre = input("Nombre del curso: ").strip()
            cursos.append(Curso(cod, nombre))
        elif opcion == "2":
            ide = input("ID del profesor: ").strip()
            nombre = input("Nombre del profesor: ").strip()
            profesores.append(Profesor(ide, nombre))
        elif opcion == "3":
            cod = input("Código del curso: ").strip()
            curso = next((c for c in cursos if c.codigo == cod), None)
            if not curso:
                print("Curso no encontrado.")
                continue
            ide = input("ID del profesor: ").strip()
            prof = next((p for p in profesores if p.identificacion == ide), None)
            if prof:
                curso.asignar_profesor(prof)
                print("Profesor asignado.")
            else:
                print("Profesor no encontrado.")
        elif opcion == "4":
            cod = input("Código del curso: ").strip()
            curso = next((c for c in cursos if c.codigo == cod), None)
            if not curso:
                print("Curso no encontrado.")
                continue
            ide = input("ID del estudiante: ").strip()
            nombre = input("Nombre del estudiante: ").strip()
            curso.matricular_estudiante(Estudiante(ide, nombre))
            print("Estudiante matriculado.")
        elif opcion == "5":
            cod = input("Código del curso: ").strip()
            curso = next((c for c in cursos if c.codigo == cod), None)
            if not curso:
                print("Curso no encontrado.")
                continue
            ide = input("ID del estudiante: ").strip()
            e = curso.buscar_estudiante(ide)
            if e:
                nota = float(input("Calificación: "))
                e.registrar_calificacion(nota)
                print("Calificación registrada.")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "6":
            cod = input("Código del curso: ").strip()
            curso = next((c for c in cursos if c.codigo == cod), None)
            if not curso:
                print("Curso no encontrado.")
                continue
            ide = input("ID del estudiante: ").strip()
            e = curso.buscar_estudiante(ide)
            if e:
                print(f"Estudiante: {e.nombre} | Promedio: {e.calcular_promedio():.2f}")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "7":
            if not cursos:
                print("No hay cursos registrados.")
            for c in cursos:
                c.mostrar_informacion()
        elif opcion == "8":
            break


if __name__ == "__main__":
    menu()
