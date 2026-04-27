import tkinter as tk
from tkinter import messagebox


class LivroView:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Livraria MVC-10419556")
        self.root.geometry("800x600")

        self.controller = None

        tk.Label(self.root, text="Título").pack()
        self.entry_titulo = tk.Entry(self.root, width=40)
        self.entry_titulo.pack()

        tk.Label(self.root, text="Autor").pack()
        self.entry_autor = tk.Entry(self.root, width=40)
        self.entry_autor.pack()

        tk.Label(self.root, text="Categoria").pack()
        self.entry_categoria = tk.Entry(self.root, width=40)
        self.entry_categoria.pack()

        tk.Label(self.root, text="Preço").pack()
        self.entry_preco = tk.Entry(self.root, width=40)
        self.entry_preco.pack()

        tk.Button(
            self.root,
            text="Cadastrar Livro",
            command=self.cadastrar_click
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Listar Livros",
            command=self.listar_click
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Excluir Livro",
            command=self.excluir_click
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Encerrar Sistema",
            command=self.fechar
        ).pack(pady=5)

        self.lista = tk.Listbox(self.root, width=80, height=15)
        self.lista.pack(pady=15)

    def set_controller(self, controller):
        self.controller = controller

    def cadastrar_click(self):
        self.controller.cadastrar_livro()

    def listar_click(self):
        self.controller.listar_livros()

    def excluir_click(self):
        self.controller.excluir_livro()

    def fechar(self):
        self.root.destroy()

    def obter_dados(self):
        return {
            "titulo": self.entry_titulo.get(),
            "autor": self.entry_autor.get(),
            "categoria": self.entry_categoria.get(),
            "preco": float(self.entry_preco.get().replace(",", "."))
        }

    def obter_indice_selecionado(self):
        selecionado = self.lista.curselection()

        if not selecionado:
            return None

        return selecionado[0]

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def mostrar_mensagem(self, texto):
        messagebox.showinfo("Sistema", texto)

    def mostrar_livros(self, livros):
        self.lista.delete(0, tk.END)

        for livro in livros:
            self.lista.insert(
                tk.END,
                f"{livro['titulo']} | "
                f"{livro['autor']} | "
                f"{livro['categoria']} | "
                f"R$ {livro['preco']}"
            )

    def iniciar(self):
        self.root.mainloop()
