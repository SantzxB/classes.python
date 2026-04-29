import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email :str
    telefone: float
@dataclass
class Funcionario:
    nome: str
    matricula : float
    email: str
    setor: str

cliente1 = Cliente("Maria", "maria@gmail.com" , "2777-3489")

print("\n DADOS DO CLIENTE \n")
print(f"Nome: {cliente1.nome}")
print(f"Gmail: {cliente1.email}")
print(f"Telefone:(71){cliente1.telefone}")

print("\n DADOS DO FUNCIONÁRIO \n")
funcionario1 = Funcionario("Roberto", "892", "Robertodanado@gmail.com", "Administrativo")

print(f"Nome: {funcionario1.nome} \nMatricula: {funcionario1.matricula} \nEmail: {funcionario1.email} \nSetor: {funcionario1.setor}")
