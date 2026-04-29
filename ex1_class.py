import os

os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int
    gmail: str
    telefone:float
@dataclass
class Pet:
    nome :str
    idade: int

#Exemplo de uso da classe

pessoa1 = Pessoa("Caio", "Santana", 18 , "Caio@gmail.com", "2282-8232")
pessoa2 = Pessoa("Bruno", "Cardoso", 78, "Cardoso123@gmail.com", "9090-0900") 
pet1 = Pet("BOB", 4)
pet2 = Pet("Jade", 6)


print(f"Nome:{pessoa1.nome} {pessoa1.sobrenome} \nIdade:{pessoa1.idade}")
print(f"Gmail: {pessoa1.gmail} \nTelefone: {pessoa1.telefone}")
print(f"Nome do Pet: {pet1.nome} \n Idade do Pet: {pet1.idade}")
print(f"\nNome: {pessoa2.nome} {pessoa2.sobrenome} \nIdade: {pessoa2.idade}")
print(f"Gmail: {pessoa2.gmail} \nTelefone: {pessoa2.telefone}")
print(f"Nome do Pet: {pet2.nome} \nIdade do Pet: {pet2.idade}")
