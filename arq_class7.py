

import os
from dataclasses import dataclass

import time

os.system("cls||clear")
op = 0

def limpar():
    os.system("cls||clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float


    def mostrar_dados(self):
        print(F"Nome do Livro: {self.nome}")
        print(f"Autor: {self.autor}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço do Livro: {self.preco} \n")


lista_livro = []


while True:
    print("\n SISTEMA DE CADASTRO \n")
    print("""
            1      ADICIONAR LIVRO
            2       LISTAR LIVRO
            3           SAIR
""")
    op = int(input("Qual função deseja?(Digite 1,2 ou 3): \n"))
    match op:
        case 1:
            
            while True:
                limpar()
                livro_novo= Livro(
                    nome=input("Nome do Livro: "),
                    autor= input("Autor: "),
                    categoria= input("Categoria do Livro: "),
                    preco= float(input("Preço do Livro: "))
                )
                print('')
                lista_livro.append(livro_novo)

                print("\nSalvando dados \n")

                with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
                    for livro in lista_livro:
                        arquivo.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preco}\n")
                    print('Salvo com sucesso')
                
                            
                novo_livro = input("Deseja Adicionar um novo Livro (s/n)? ")
                if novo_livro == "s":
                    continue
                elif novo_livro == "n":
                    break
                else:
                    print(" Resposta não compreendida!")
                    break
    
        case 2:
            os.system("cls")
            @dataclass
            class Livro:
                nome:str
                autor:str
                categoria: str
                preco: float

                def mostrar_dados(self):
                    print(f"Nome do Livro: {self.nome}")
                    print(f"Autor: {self.autor}")
                    print(f"Categoria do Livro: {self.categoria}\n")
                    print(f"Preço do Livro: {self.preco}")

            lista_livro = []

            with open('catalogo_livros.csv', 'r', encoding= 'utf-8') as arquivo:
                for linha in arquivo:
                    nome, autor, categoria, preco = linha.strip().split(',')
                    lista_livro.append(Livro(
                        nome=nome,
                        autor=autor,
                        categoria=categoria,
                        preco=preco
                    ))

            for i in range(2):
                limpar()
                print("Carregando Livros...")
                time.sleep(1)

            for livro in lista_livro:
                livro.mostrar_dados()
                time.sleep(0.7)
        case 3:
            break
        case _:
            print("Opção inválida!")
