import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Login")

        tk.Label(root, text="Usuario:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(root, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(root, text="Iniciar sesión", command=self.intentar_login).grid(row=2, column=0, columnspan=2, pady=10)

    def intentar_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controlador.verificar_credenciales(username, password):
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")


class InventarioView:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Gestión de Inventario")

        tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)

        tk.Label(root, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(root, text="Descripción:").grid(row=2, column=0, padx=10, pady=5)
        self.descripcion_entry = tk.Entry(root)
        self.descripcion_entry.grid(row=2, column=1)

        tk.Button(root, text="Agregar Equipo", command=self.agregar_equipo).grid(row=3, column=0, columnspan=2, pady=10)

        self.equipos_listbox = tk.Listbox(root, width=100)
        self.equipos_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def agregar_equipo(self):
        id_equipo = self.id_entry.get()
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()

        if id_equipo and nombre and descripcion:
            self.controlador.agregar_equipo(id_equipo, nombre, descripcion)
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def actualizar_lista(self):
        self.equipos_listbox.delete(0, tk.END)
        for equipo in self.controlador.obtener_equipos():
            self.equipos_listbox.insert(tk.END, str(equipo))

