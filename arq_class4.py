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

for funcionario in lista_funcionario:
    funcionario.mostrar_dados()
