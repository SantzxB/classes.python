

import os
from dataclasses import dataclass

import time

os.system("cls||clear")

def limpar():
    os.system("cls||clear")

@dataclass
class Empresa:
    nome: str
    cnpj:int
    telefone : int

    def mostrar_dados(self):
        print(F"Nome da Empresa: {self.nome}")
        print(f"CNJP: {self.cnpj}\n")
        print(f"Telefone: {self.telefone}")


lista_empresa = []

print("\nSolicitando Dados\n")

while True:
    nova_empresa= Empresa(
        nome=input("Nome da Empresa: "),
        cnpj=int(input("CNPJ: ")),
        telefone=int(input("Telefone para contato: "))
    )
    print('')
    lista_empresa.append(nova_empresa)

    empresa_nova = input("Deseja Adicionar uma nova Empresa (s/n)? ")
    if empresa_nova == "s":
        continue
    elif empresa_nova == "n":
        break
    else:
        print(" Resposta não compreendida!")
        break
print("\nSalvando dados \n")
with open('Contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
        for empresa in lista_empresa:
            arquivo.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n")
        print('Salvo com sucesso')

@dataclass
class Empresa:
    nome:str
    cnpj:str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome da Empresa: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Telefone de contato: {self.telefone}\n")

lista_empresa = []

with open('contato_empresas.csv', 'r', encoding= 'utf-8') as arquivo:
    for linha in arquivo:
        nome, cnpj, telefone = linha.strip().split(',')
        lista_empresa.append(Empresa(
            nome=nome,
            cnpj=cnpj,
            telefone=telefone
        ))

for i in range(2):
    limpar()
    print("Carregando empresas...")
    time.sleep(2)

for empresa in lista_empresa:
    empresa.mostrar_dados()
    time.sleep(0.7)
