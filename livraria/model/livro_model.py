class LivroModel:

    def __init__(self):
        self.livros = [
            {"titulo": "Livro A", "autor": "Autor 1", "categoria": "Ficção", "preco": 30},
            {"titulo": "Livro B", "autor": "Autor 2", "categoria": "Técnico", "preco": 50},
            {"titulo": "Livro C", "autor": "Autor 1", "categoria": "Ficção", "preco": 40},
        ]

    def listar_livros(self):
        return self.livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def excluir_livro(self, indice):
        if 0 <= indice < len(self.livros):
            del self.livros[indice]
