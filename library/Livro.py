class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Status: {self.status}"