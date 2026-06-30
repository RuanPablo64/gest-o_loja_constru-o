import funcoes_gerais
from funcoes_gerais import logo
from funcoes_gerais import limpador
from cadastro import cadastro_produto
from procurar import procurar_produto
from atualizar import atualizar_produtos
from excluir import excluir_produto
def modulo_produtos(produtos):
    decisao_produtos = "0"
    while decisao_produtos != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+      Modulo Produtos      +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#      1 - Cadastrar        #")
            print("#      2 - Visualizar       #")
            print("#      3 - Ajustar          #")
            print("#      4 - Excluir          #")
            print("#      5 - Sair do Modulo   #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_produtos = input("por favor, escolha uma das opções listadas: ")
            if decisao_produtos == "1":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Cadastrar produto    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                cadastro_produto(produtos)
            elif decisao_produtos == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Procurar produtos    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                procurar_produto(produtos)
            elif decisao_produtos == "3":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Alterar produtos     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                alteracao = input("digite o codigo do produto que deseja alterar: ")
                if alteracao in produtos:
                    print(f"nome do produto: {produtos[alteracao]["nome"]}")
                    print(f"preço do produto: {produtos[alteracao]["preço"]}")
                    print(f"categoria do produto: {produtos[alteracao]["categoria"]}")
                    print(f"disponibilidade do produto: {produtos[alteracao]["estoque"]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    atualizar_produtos(produtos, alteracao)
                else:
                    print("o produto que você quer alterar não está cadastrado no sistema")
                    print()
                    sair = input("aperte <enter> para sair: ")
            elif decisao_produtos == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+    exclusão de produtos   +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir_produto(produtos)
            elif not (decisao_produtos.isdigit()) or (decisao_produtos <= "0" or decisao_produtos > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")