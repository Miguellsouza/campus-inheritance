from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de pater ponto")

    def __str__(self):
        return f"O(A) funcionário(A) {self.nome}, tem {self.idade} anos, trabalha de {self.cargo} no setor do(a) {self.setor}"