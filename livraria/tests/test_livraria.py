import unittest
from livraria.model.livro_model import LivroModel


class TestLivrariaMVC(unittest.TestCase):

    def test_listar_livros(self):
        model = LivroModel()
        self.assertEqual(len(model.listar_livros()), 3)

    def test_adicionar_livro(self):
        model = LivroModel()

        model.adicionar_livro({
            "titulo": "Novo",
            "autor": "Autor X",
            "categoria": "Drama",
            "preco": 45
        })

        self.assertEqual(len(model.listar_livros()), 4)

    def test_excluir_livro(self):
        model = LivroModel()

        model.excluir_livro(0)

        self.assertEqual(len(model.listar_livros()), 2)


if __name__ == "__main__":
    unittest.main()
