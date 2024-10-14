from Membro import *
from Livro import *

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []
        self.membros = []

    def inc_livro(self, id, titulo, autor):
        novo_livro = Livro(id, titulo, autor)
        self.catalogo.append(novo_livro)
        return f"Livro '{titulo}' adicionado ao catálogo."

    def inc_membro(self, numero, nome):
        novo_membro = Membro(numero, nome)
        self.membros.append(novo_membro)
        return f"Membro '{nome}' adicionado à biblioteca."

    def emprestar_livro(self, id_livro, numero_membro):
        livro = next((livro for livro in self.catalogo if livro.id == id_livro), None)
        membro = next((membro for membro in self.membros if membro.numero == numero_membro), None)
        if livro and membro:
            if livro.status == "disponível":
                livro.status = "emprestado"
                membro.adicionar_historico(livro)
                return f"Livro '{livro.titulo}' emprestado para o membro '{membro.nome}'."
            else:
                return f"Livro '{livro.titulo}' já está emprestado."
        else:
            return "Livro ou membro não encontrado."

    def devolver_livro(self, id_livro):
        livro = next((livro for livro in self.catalogo if livro.id == id_livro), None)
        if livro:
            if livro.status == "emprestado":
                livro.status = "disponível"
                return f"Livro '{livro.titulo}' devolvido."
            else:
                return f"Livro '{livro.titulo}' já está disponível no catálogo."
        else:
            return "Livro não encontrado."