class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def autenticar(self, username, password):
        return self.username == username and self.password == password


class Equipo:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}"


class Inventario:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def obtener_equipos(self):
        return self.equipos
