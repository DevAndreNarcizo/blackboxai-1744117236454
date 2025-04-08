# Este é o ponto de entrada para o aplicativo de gestão financeira pessoal.

import tkinter as tk
from tkinter import messagebox
from dashboard import mostrar_dashboard

def adicionar_receita():
    # Função para adicionar receita
    pass

def adicionar_despesa():
    # Função para adicionar despesa
    pass

def main():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Gestão Financeira Pessoal")
    root.geometry("600x400")

    # Criar um menu
    menu = tk.Menu(root)
    root.config(menu=menu)

    # Adicionar opções ao menu
    menu.add_command(label="Dashboard", command=mostrar_dashboard)
    menu.add_command(label="Adicionar Receita", command=adicionar_receita)
    menu.add_command(label="Adicionar Despesa", command=adicionar_despesa)

    # Iniciar a interface
    root.mainloop()

if __name__ == "__main__":
    main()
