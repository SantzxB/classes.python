import os

os.system("cls")
from dataclasses import dataclass

@dataclass
class Cliente:
    nome:str
    email:str
    telefone:str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
    
print("\n Solicitando Dados \n")

cliente = Cliente(
    nome=input("Nome: "), 
    email=input("Email: "), 
    telefone=input("Telefone: ")
)

print("\n Exibindo Dados do Cliente \n")

cliente.mostrar_dados()
