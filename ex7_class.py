import os

os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    lagradouro: str
    numero: str

@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco #Relacionamento com a classe Endereco
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.lagradouro}")
        print(f"Número: {self.endereco.numero}")
print("\n Solicitando Dados \n")
cliente = Cliente(
    nome=input("Digite seu nome:"),
    idade=input("Digite sua idade: "),
    endereco = Endereco(
        lagradouro=input("Endereço: "),
    numero=input("número da residência: ")
)

    )
print("\n Exibindo seus Dados \n")

cliente.mostrar_dados()
