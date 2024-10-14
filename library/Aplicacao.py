from Biblioteca import *

class Aplicacao:
    def __init__(self, nome_bib):
        self.bib = Biblioteca(nome_bib)
        while True:
            print(f'''
=======================
Biblioteca {self.bib.nome}
=======================
1. Incluir um livro
2. Incluir um membro
3. Listar todos os livros
4. Listar todos os membros
5. Emprestar livro
6. Devolver livro
x. Fim
=======================
          ''')

            op = input('Escolha uma opção: ')

            if op == '1':
                self.fun_inc_livro()
            elif op == '2':
                self.fun_inc_membro()
            elif op == '3':
                self.fun_lista_livros()
            elif op == '4':
                self.fun_lista_membros()
            elif op == '5':
                self.fun_emprestimo()
            elif op == '6':
                self.fun_devolucao()
            elif op == 'x':
                break

    def fun_inc_livro(self):
        print('--------------( Incluir Livro)')
        liv_id = int(input('Informe o ID do livro:'))
        liv_titulo = input('Informe o TÍTULO do livro:')
        liv_autor = input('Informe o AUTOR do livro:')
        retorno = self.bib.inc_livro(liv_id, liv_titulo, liv_autor)
        print(retorno)

    def fun_inc_membro(self):
        print('--------------( Incluir Membro)')
        mem_num = int(input('Informe o NUMERO do membro:'))
        mem_nome = input('Informe o NOME do membro:')
        retorno = self.bib.inc_membro(mem_num, mem_nome)
        print(retorno)

    def fun_lista_livros(self):
        print('--------------( Listar Livros)')
        for livro in self.bib.catalogo:
            print(livro)
        print('--------------( Fim do relatório)')

    def fun_lista_membros(self):
        print('--------------( Listar Membros)')
        for membro in self.bib.membros:
            print(membro)
        print('--------------( Fim do relatório)')

    def fun_emprestimo(self):
        self.fun_lista_livros()
        self.fun_lista_membros()
        print('--------------( Emprestar Livro)')
        liv_id = int(input('Informe o ID do livro:'))
        mem_num = int(input('Informe o NUMERO do membro:'))
        retorno = self.bib.emprestar_livro(liv_id, mem_num)
        print(retorno)

    def fun_devolucao(self):
        self.fun_lista_livros()
        print('--------------( Devolver Livro)')
        liv_id = int(input('Informe o ID do livro:'))
        retorno = self.bib.devolver_livro(liv_id)
        print(retorno)

if __name__ == '__main__':
    biblioteca = Aplicacao('Infinity Books')
else:
    print('este arquivo DEVE ser executado diretamente')