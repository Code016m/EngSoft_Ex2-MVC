from livraria.model.livro_model import LivroModel
from livraria.view.livro_view import LivroView


class LivroController:

    def __init__(self):
        self.model = LivroModel()
        self.view = LivroView()
        self.view.set_controller(self)

    def cadastrar_livro(self):
        try:
            livro = self.view.obter_dados()

            self.model.adicionar_livro(livro)

            self.view.limpar_campos()
            self.view.mostrar_mensagem("Livro cadastrado com sucesso!")

            self.listar_livros()

        except Exception as e:
            self.view.mostrar_mensagem(f"Erro: {str(e)}")

    def listar_livros(self):
        livros = self.model.listar_livros()
        self.view.mostrar_livros(livros)

    def excluir_livro(self):
        indice = self.view.obter_indice_selecionado()

        if indice is None:
            self.view.mostrar_mensagem("Selecione um livro.")
            return

        self.model.excluir_livro(indice)

        self.view.mostrar_mensagem("Livro excluído com sucesso!")
        self.listar_livros()

    def iniciar(self):
        self.view.iniciar()
