import os

os.system("cls")
from dataclasses import dataclass

@dataclass
class Fornecedor:
    nome:str
    email:str
    telefone:str
    endereco:str
print("\n Solicitando Dados do Fornecedor \n")

fornecedor= Fornecedor(
    nome=input("Nome: "), 
    email=input("Email: "), 
    telefone=input("Telefone: "),
    endereco=input("Endereço: "))

print("\n Exibindo Dados do Cliente \n")

print(f"Nome: {fornecedor.nome}")
print(f"Email: {fornecedor.email}")
print(f"Telefone: (71){fornecedor.telefone}")
print(f"Endereço: {fornecedor.endereco}")
