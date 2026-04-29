import os

os.system("cls")
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

print("\n Solicitando Dados do Paciente \n")

paciente = Paciente(
    nome =input("Nome do Paciente: "),
    idade =input("Idade do Paciente: "),
    peso =input("Peso do Paciente: "), 
    altura =input("Altura do Paciente: ")
)

print("\n Dados do Paciente \n")

print(f"Nome: {paciente.nome}")
print(f"Idade: {paciente.idade}")
print(f"Peso: {paciente.peso}")
print(f"Altura: {paciente.altura}")
