from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

aluno1 = Aluno("Manuel", 9, "ADS", 12)
aluno1.fazer_aniversario()
aluno1.fazer_matricula()
print(aluno1)

professor1 = Professor("Samuel", 37, "Biologia", "Mestrado")
professor1.fazer_aniversario()
professor1.dar_aula()
print(professor1)

funcionario1 = Funcionario("Cláudia", 27, "Secretária", "Secretaria")
funcionario1.fazer_aniversario()
funcionario1.bater_ponto()
print(funcionario1)