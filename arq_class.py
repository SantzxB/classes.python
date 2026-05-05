import os
from dataclasses import dataclass
os.system("cls||clear")


@dataclass
class Funcionario:
    nome: str
    idade:int

    def mostrar_dados(self):
        print(F"Nome: {self.nome}")
        print(f"Idade: {self.idade}\n")

quantidade_funcionarios =  2
lista_funcionarios = []

print("\nSolicitando Dados\n")

for i in range(quantidade_funcionarios):
    novo_funcionario = Funcionario(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: "))
    )
    print('')
    lista_funcionarios.append(novo_funcionario)

print("\n Exibindo Dados \n")
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

print("\nSalvando dados \n")
with open('lista funcionarios.csv', 'a', encoding='utf-8') as arquivo:
        for funcionario in lista_funcionarios:
            arquivo.write(f"{funcionario.nome}, {funcionario. idade}\n")
        print('Salvo com sucesso')

print('- Fim do programa. -')
