import os
from dataclasses import dataclass
import time

ARQUIVO = "catalogo_carros.csv"

def limpar():
    os.system("cls||clear")

@dataclass
class Carro:
    modelo: str
    marca: str
    ano: int

    def mostrar_dados(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print("-" * 20)


def salvar_carro(carro: Carro):
    with open(ARQUIVO, 'a', encoding='utf-8') as f:
        f.write(f"{carro.modelo},{carro.marca},{carro.ano}\n")


def carregar_carros():
    carros = []
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            for linha in f:
                modelo, marca, ano = linha.strip().split(',')
                carros.append(Carro(modelo, marca, int(ano)))
    except FileNotFoundError:
        pass
    return carros


def adicionar_carro():
    while True:
        limpar()
        try:
            carro = Carro(
                modelo=input("Modelo: "),
                marca=input("Marca: "),
                ano=int(input("Ano: "))
            )
        except ValueError:
            print("Ano inválido! Digite um número.")
            time.sleep(1.5)
            continue

        salvar_carro(carro)
        print("\nSalvo com sucesso!")

        op = input("Adicionar outro? (s/n): ").lower()
        if op != 's':
            break


def listar_carros():
    limpar()
    carros = carregar_carros()

    if not carros:
        print("Nenhum carro cadastrado.")
        return

    print("Carregando carros...")
    time.sleep(1)

    for carro in carros:
        carro.mostrar_dados()
        time.sleep(0.5)


def menu():
    while True:
        print("\n SISTEMA DE CADASTRO \n")
        print("1 - Adicionar carro")
        print("2 - Listar carros")
        print("3 - Sair")

        try:
            op = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        match op:
            case 1:
                adicionar_carro()
            case 2:
                listar_carros()
            case 3:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    menu()
