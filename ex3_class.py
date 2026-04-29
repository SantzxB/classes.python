import os

os.system("cls")
from dataclasses import dataclass

@dataclass
class Cliente:
    nome:str
    email:str
    telefone:str
    
print("\n Solicitando Dados \n")

cliente = Cliente(
    nome=input("Nome: "), 
    email=input("Email: "), 
    telefone=input("Telefone: ")
)

print("\n Exibindo Dados do Cliente \n")

print(f"Nome: {cliente.nome}")
print(f"Email: {cliente.email}")
print(f"Telefone: {cliente.telefone}")
