from datetime import date

class Amigo:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.telefone} - {self.email})"


class DVD:
    def __init__(self, id, titulo, sinopse, diretor, ator, genero, faixa):
        self.id = id
        self.titulo = titulo
        self.sinopse = sinopse
        self.diretor = diretor
        self.ator = ator
        self.genero = genero
        self.faixa = faixa

    def __str__(self):
        return f"{self.titulo} - {self.genero} ({self.faixa})"


class Emprestimo:
    def __init__(self, id, amigo, dvd, data_emprestimo, data_devolucao=None, observacoes=""):
        self.id = id
        self.amigo = amigo
        self.dvd = dvd
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.observacoes = observacoes

    def __str__(self):
        devolucao = self.data_devolucao if self.data_devolucao else "Em andamento"
        return (f"Empréstimo #{self.id} - {self.dvd.titulo} para {self.amigo.nome}\n"
                f"Data: {self.data_emprestimo} | Devolução: {devolucao}\n"
                f"Observações: {self.observacoes}")


# 🔧 Exemplo de uso

amigo1 = Amigo(1, "João", "99999-9999", "joao@email.com")
dvd1 = DVD(1, "Matrix", "Realidade simulada", "Wachowski", "Keanu Reeves", "Ação", "16+")
emprestimo1 = Emprestimo(1, amigo1, dvd1, date(2025, 4, 24))

print(emprestimo1)
