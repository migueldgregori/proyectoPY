import tkinter as tk
from vista import LoginView, InventarioView
from controlador import Controlador


def main():
    controlador = Controlador()

    # Ventana de Login
    root_login = tk.Tk()
    login_view = LoginView(root_login, controlador)
    root_login.mainloop()

    # abre la ventana de Inventario
    if controlador.verificar_credenciales("admin", "1234"):
        root_inventario = tk.Tk()
        inventario_view = InventarioView(root_inventario, controlador)
        root_inventario.mainloop()


if __name__ == "__main__":
    main()
