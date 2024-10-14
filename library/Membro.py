class Membro:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.historico_emprestimos = []

    def adicionar_historico(self, livro):
        self.historico_emprestimos.append(livro)

    def __str__(self):
        return f"Número do Membro: {self.numero} | Nome: {self.nome} | Histórico: {self.historico_emprestimos}"