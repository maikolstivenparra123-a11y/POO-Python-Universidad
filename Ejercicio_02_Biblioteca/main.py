class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"


class Usuario:
    def __init__(self, id_usuario: str, nombre: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self) -> str:
        return f"ID: {self.id_usuario} | Nombre: {self.nombre}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_libro(self, libro: Libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, isbn: str):
        for l in self.libros:
            if l.isbn == isbn:
                return l
        return None

    def buscar_usuario(self, id_usuario: str):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def realizar_prestamo(self, isbn: str, id_usuario: str):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id_usuario)
        if libro and usuario and libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            print("Préstamo realizado con éxito.")
        else:
            print("No se pudo realizar el préstamo.")

    def realizar_devolucion(self, isbn: str, id_usuario: str):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id_usuario)
        if libro and usuario and libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            print("Devolución realizada con éxito.")
        else:
            print("No se pudo realizar la devolución.")

    def consultar_disponibles(self):
        disponibles = [l for l in self.libros if l.disponible]
        if not disponibles:
            print("No hay libros disponibles.")
        for l in disponibles:
            print(l)

    def mostrar_prestamos_activos(self):
        hay = False
        for u in self.usuarios:
            if u.libros_prestados:
                hay = True
                print(f"Usuario: {u.nombre}")
                for l in u.libros_prestados:
                    print(f"  Libro: {l.titulo} (ISBN: {l.isbn})")
        if not hay:
            print("No hay préstamos activos.")


def menu():
    biblio = Biblioteca()
    while True:
        print("\n1. Registrar libro\n2. Registrar usuario\n3. Realizar préstamo\n4. Realizar devolución\n5. Consultar libros disponibles\n6. Mostrar préstamos activos\n7. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            isbn = input("ISBN: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            biblio.registrar_libro(Libro(isbn, titulo, autor))
        elif opcion == "2":
            id_u = input("ID Usuario: ").strip()
            nombre = input("Nombre: ").strip()
            biblio.registrar_usuario(Usuario(id_u, nombre))
        elif opcion == "3":
            isbn = input("ISBN del libro: ").strip()
            id_u = input("ID del usuario: ").strip()
            biblio.realizar_prestamo(isbn, id_u)
        elif opcion == "4":
            isbn = input("ISBN del libro: ").strip()
            id_u = input("ID del usuario: ").strip()
            biblio.realizar_devolucion(isbn, id_u)
        elif opcion == "5":
            biblio.consultar_disponibles()
        elif opcion == "6":
            biblio.mostrar_prestamos_activos()
        elif opcion == "7":
            break


if __name__ == "__main__":
    menu()
