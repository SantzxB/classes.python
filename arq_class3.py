import os 
from dataclasses import dataclass


os.system("cls||clear")

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

for empresa in lista_empresa:
    empresa.mostrar_dados()
