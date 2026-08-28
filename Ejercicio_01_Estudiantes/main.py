class Estudiante:
    def __init__(self, nombre: str, identificacion: str, programa: str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.programa = programa
        self.notas = []

    def registrar_nota(self, nota: float):
        if 0.0 <= nota <= 5.0:
            self.notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def determinar_estado(self) -> str:
        if not self.notas:
            return "Sin notas"
        return "Aprobado" if self.calcular_promedio() >= 3.0 else "Reprobado"

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Programa: {self.programa} | Promedio: {self.calcular_promedio():.2f} | Estado: {self.determinar_estado()}"


class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, identificacion: str):
        for e in self.estudiantes:
            if e.identificacion == identificacion:
                return e
        return None

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        for e in self.estudiantes:
            print(e)


def menu():
    gestion = GestionEstudiantes()
    while True:
        print("\n1. Registrar estudiante\n2. Registrar nota\n3. Calcular promedio y estado\n4. Mostrar estudiantes\n5. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            ide = input("Identificación: ").strip()
            programa = input("Programa: ").strip()
            gestion.agregar_estudiante(Estudiante(nombre, ide, programa))
        elif opcion == "2":
            ide = input("Identificación del estudiante: ").strip()
            e = gestion.buscar_estudiante(ide)
            if e:
                nota = float(input("Nota: "))
                e.registrar_nota(nota)
            else:
                print("Estudiante no encontrado.")
        elif opcion == "3":
            ide = input("Identificación del estudiante: ").strip()
            e = gestion.buscar_estudiante(ide)
            if e:
                print(f"Promedio: {e.calcular_promedio():.2f} | Estado: {e.determinar_estado()}")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "4":
            gestion.mostrar_estudiantes()
        elif opcion == "5":
            break


if __name__ == "__main__":
    menu()
