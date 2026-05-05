import os
from dataclasses import dataclass
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

quantidade_empresa =  2
lista_empresa = []

print("\nSolicitando Dados\n")

for i in range(quantidade_empresa):
    nova_empresa= Empresa(
        nome=input("Nome da Empresa: "),
        cnpj=int(input("CNPJ: ")),
        telefone=int(input("Telefone para contato: "))
    )
    print('')
    lista_empresa.append(nova_empresa)

print("\n Exibindo Dados \n")
for empresa in lista_empresa:
    empresa.mostrar_dados()

print("\nSalvando dados \n")
with open('Contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
        for empresa in lista_empresa:
            arquivo.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n")
        print('Salvo com sucesso')

print('- Fim do prograns. -')
