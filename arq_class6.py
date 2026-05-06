import os
from dataclasses import dataclass

import time


os.system("cls||clear")

def limpar():
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

import os
from dataclasses import dataclass


os.system("cls||clear")

@dataclass
class Funcionario:
    nome:str
    idade: str

    def mostrar_dados(self):
        print(f"Nome do Funcionário: {self.nome}")
        print(f"Idade do Funcionário: {self.idade}")


lista_funcionario = []

with open('lista funcionarios.csv', 'r', encoding= 'utf-8') as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(',')
        lista_funcionario.append(Funcionario(
            nome=nome,
            idade=idade,
            
        ))
for i in range(3):
    limpar()
    print("Carregando...")
    time.sleep(2)


for funcionario in lista_funcionario:
    funcionario.mostrar_dados()
    time.sleep(0.7)
