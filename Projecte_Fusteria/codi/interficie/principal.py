"""
Finestra principal del programa de gestió de fusteria.
"""

import tkinter as tk
from tkinter import messagebox

class FinestraPrincipal:
    def __init__(self, arrel):
        self.arrel = arrel
        self.arrel.title("Gestió de Fusteria")
        self.arrel.geometry("800x600")
        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self.arrel)

        # Menú "Mòduls"
        menu_moduls = tk.Menu(barra_menu, tearoff=0)
        menu_moduls.add_command(label="Clients", command=self.obrir_clients)
        menu_moduls.add_command(label="Facturació", command=self.obrir_facturacio)
        menu_moduls.add_command(label="Comptabilitat", command=self.obrir_comptabilitat)
        menu_moduls.add_command(label="Laboral", command=self.obrir_laboral)
        menu_moduls.add_command(label="Tasques", command=self.obrir_tasques)
        menu_moduls.add_command(label="Estadístiques", command=self.obrir_estadistiques)
        barra_menu.add_cascade(label="Mòduls", menu=menu_moduls)

        # Menú "Configuració"
        menu_configuracio = tk.Menu(barra_menu, tearoff=0)
        menu_configuracio.add_command(label="Preferències", command=self.obrir_configuracio)
        barra_menu.add_cascade(label="Configuració", menu=menu_configuracio)

        # Menú "Ajuda"
        menu_ajuda = tk.Menu(barra_menu, tearoff=0)
        menu_ajuda.add_command(label="Quant a", command=self.mostrar_quant_a)
        barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

        # Opció de sortir
        barra_menu.add_command(label="Sortir", command=self.arrel.quit)

        self.arrel.config(menu=barra_menu)

    # Funcions de menú (de moment només missatges)
    def obrir_clients(self):
        messagebox.showinfo("Clients", "Gestió de clients (pendent d’implementar).")

    def obrir_facturacio(self):
        messagebox.showinfo("Facturació", "Gestió de factures (pendent d’implementar).")

    def obrir_comptabilitat(self):
        messagebox.showinfo("Comptabilitat", "Mòdul comptable (pendent d’implementar).")

    def obrir_laboral(self):
        messagebox.showinfo("Laboral", "Gestió laboral (pendent d’implementar).")

    def obrir_tasques(self):
        messagebox.showinfo("Tasques", "Seguiment de tasques (pendent d’implementar).")

    def obrir_estadistiques(self):
        messagebox.showinfo("Estadístiques", "Visualització d'estadístiques (pendent d’implementar).")

    def obrir_configuracio(self):
        messagebox.showinfo("Configuració", "Preferències de l’usuari (pendent d’implementar).")

    def mostrar_quant_a(self):
        messagebox.showinfo("Quant a", "Aplicació de gestió per a una fusteria.Versió 0.1")

if __name__ == "__main__":
    arrel = tk.Tk()
    app = FinestraPrincipal(arrel)
    arrel.mainloop()
