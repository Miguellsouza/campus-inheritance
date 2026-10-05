from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof.{self.nome} começou a dar aula")

    def __str__(self):
        return f"Prof.{self.nome}, tem {self.idade} anos, tem o cargo de professor de {self.especialidade} com {self.nivel}"
