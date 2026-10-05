from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula")

    def __str__(self):
        return f"Aluno {self.nome}, tem {self.idade} anos, e está na turma {self.turma} do curso {self.curso}"