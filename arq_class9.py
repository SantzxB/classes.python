import os
from dataclasses import dataclass
import time

os.system("cls||clear")

ARQUIVO = "catalogo_jogos.csv"

def limpar():
    os.system("cls||clear")

@dataclass
class Jogo:
    nome: str
    categoria: str
    ano: int
    preco: float
    empresa: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Empresa: {self.empresa}")
        print("-" * 25)
#@dataclass
#class Personagem:
#   nome:str
#   genero: str
    

def salvar_jogo(jogo: Jogo):
    with open(ARQUIVO, 'a', encoding='utf-8') as f:
        f.write(f"{jogo.nome},{jogo.categoria},{jogo.ano},{jogo.preco},{jogo.empresa}\n")


def carregar_jogos():
    jogos = []
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            for linha in f:
                nome, categoria, ano, preco, empresa = linha.strip().split(',')
                jogos.append(Jogo(nome, categoria, int(ano), float(preco), empresa))
    except FileNotFoundError:
        pass
    return jogos


def adicionar_jogo():
    while True:
        limpar()
        try:
            jogo = Jogo(
                nome=input("Nome do jogo: "),
                categoria=input("Categoria: "),
                ano=int(input("Ano: ")),
                preco=float(input("Preço: ")),
                empresa=input("Empresa: ")
            )
        except ValueError:
            print("Ano ou preço inválido! Tente novamente.")
            time.sleep(1.5)
            continue

        salvar_jogo(jogo)
        print("\nSalvo com sucesso!")

        op = input("Adicionar outro? (s/n): ").lower()
        if op != 's':
            break


def listar_jogos():
    limpar()
    jogos = carregar_jogos()

    if not jogos:
        print("Nenhum jogo cadastrado.")
        return

    print("Carregando jogos...")
    time.sleep(1)

    for jogo in jogos:
        jogo.mostrar_dados()
        time.sleep(0.5)


def menu():
    while True:
        print("\n SISTEMA DE CADASTRO \n")
        print("1 - Adicionar jogo")
        print("2 - Listar jogos")
        print("3 - Sair")

        try:
            op = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        match op:
            case 1:
                adicionar_jogo()
            case 2:
                listar_jogos()
            case 3:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    menu()
