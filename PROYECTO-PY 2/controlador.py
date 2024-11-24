from modelo import Usuario, Equipo, Inventario


class Controlador:
    def __init__(self):
        self.usuario = Usuario("admin", "1234")
        self.inventario = Inventario()

    def verificar_credenciales(self, username, password):
        return self.usuario.autenticar(username, password)

    def agregar_equipo(self, id, nombre, descripcion):
        equipo = Equipo(id, nombre, descripcion)
        self.inventario.agregar_equipo(equipo)

    def obtener_equipos(self):
        return self.inventario.obtener_equipos()
