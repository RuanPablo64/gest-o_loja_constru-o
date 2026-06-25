import funcoes_gerais
from funcoes_gerais import logo
from funcoes_gerais import limpador

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
                print()
                print()
                ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
                funcoes_gerais.validar_ean(ean, produtos)
                print()
                nome = input("digite o nome do produto: ")
                funcoes_gerais.validar_nome_produto(nome, produtos)
                print()
                preco = input("digite um preço para o produto: ")
                while not funcoes_gerais.validar_preco(preco):
                    preco = input("digite um preço para o produto: ")
                print()
                categoria = input("digite a categoria do produto: ")
                while categoria == "":
                    print("você digitou uma categoria vazia. Tente novamente")
                    categoria = input("digite a categoria do produto: ")
                print()
                estoque = "disponivel"
                print()
                produtos[ean] = {"nome" : nome, "preço" : preco, "categoria" : categoria, "estoque" : estoque}
                print(produtos)
                print()
                print("o cadastro do produto foi bem sucedido!")
                print()
                sair = input("aperte <enter> para sair: ")
            elif decisao_produtos == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Procurar produtos    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                metodo = input("de qual forma deseja procurar o produtos [codigo ean(1)/nome do produto(2)]: ")
                if metodo == "1":
                    busca = input("digite o codigo do produto que você deseja visualizar: ")
                    if busca in produtos:
                        print(f"nome do produto: {produtos[busca]["nome"]}")
                        print(f"preço do produto: {produtos[busca]["preço"]}")
                        print(f"categoria do produto: {produtos[busca]["categoria"]}")
                        print(f"disponibilidade do produto: {produtos[busca]["estoque"]}")
                        print()
                        sair = input("aperte <enter> para sair: ")
                    else:
                        print("o codigo do produto não está registrado no sistema")
                        sair = input("aperte <enter> para sair: ")
                elif metodo == "2":
                    busca_nome = input("digite o nome do produto que você deseja visualizar: ")
                    contador = 0
                    for ean in produtos:
                        if produtos[ean]["nome"].startswith(busca_nome):
                            print(f"codigo ean do produto: {ean}")
                            print(f"preço do produto: {produtos[ean]["preço"]}")
                            print(f"categoria do produto: {produtos[ean]["categoria"]}")
                            print(f"disponibilidade do produto: {produtos[ean]["estoque"]}")
                            contador += 1
                    if contador == 0:
                        print("o produto informado com esse nome não está cadastrado no sistema")
                        sair = input("aperte <enter> para sair")
                    else:
                        sair = input("aperte <enter> para sair")
                else:
                    print("você digitou uma opção invalida")
                    sair = input("aperte <enter> para sair")
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
                    decisao_alteracao = "0"
                    while decisao_alteracao != "5":
                        limpador()
                        logo()
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("+                           +")
                        print("+       1 - Nome            +")
                        print("+       2 - Preço           +")
                        print("+       3 - Categoria       +")
                        print("+       4 - Estoque         +")
                        print("+       5 - Sair            +")
                        print("+                           +")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
                        print()
                        if decisao_alteracao == "1":
                            limpador()
                            logo()
                            print()
                            nome = input("digite o novo nome do produto: ")
                            print()
                            funcoes_gerais.validar_nome_produto(nome, produtos)
                            produtos[alteracao]["nome"] = nome
                            print()
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar: ")
                        elif decisao_alteracao == "2":
                            limpador()
                            logo()
                            print()
                            preco = input("digite o novo preço do produto: ")
                            while not funcoes_gerais.validar_preco(preco):
                                print("tente novamente")
                                sair = input("aperte <enter> para sair")
                            print()
                            produtos[alteracao]["preço"] = preco
                            print()
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar: ")
                        elif decisao_alteracao == "3":
                            limpador()
                            logo()
                            print()
                            nova_categoria = input("digite a nova categoria do produto")
                            print()
                            produtos[alteracao]["categoria"] = nova_categoria
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "4":
                            limpador()
                            logo()
                            print()
                            if produtos[alteracao]["estoque"] == "disponivel":
                                print("o produto continua em estoque. Caso queira impor que ele está indisponivel, acesse a área de exclusão desse modulo")
                                print()
                                sair = input("aperte <enter> para voltar")
                            else:
                                mudanca = input("tem certeza de que o produto está de volta para o estoque?: ")
                                if mudanca.lower() == "s" or mudanca.lower() == "sim":
                                    produtos[alteracao]["estoque"] = "disponivel"
                                    print(produtos)
                                    print()
                                    print("a alteração foi bem sucedida")
                                    sair = input("aperte <enter> para voltar: ")
                                else:
                                    print("mudança cancelada!")
                                    sair = input("aperte <enter> para voltar: ")
                        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "5"):
                            print()
                            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
                            sair = input("aperte <enter> para voltar: ")
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
                excluir = input("digite o codigo do produto que deseja excluir: ")
                if excluir in produtos:
                    print()
                    print(f"nome do produto: {produtos[excluir]["nome"]}")
                    print(f"preço do produto: {produtos[excluir]["preço"]}")
                    print(f"categoria do produto: {produtos[excluir]["categoria"]}")
                    print(f"disponibilidade do produto: {produtos[excluir]["estoque"]}")
                    print()
                    if produtos[excluir]["estoque"] == "indisponivel":
                        print("o produto já se encontra fora de estoque. caso queira confirma-lo como disponivel, acesse a área de atualizações desse modulo")
                        sair = input("aperte <enter> para sair: ")
                    else:
                        certeza = input("você tem certeza de que deseja excluir esse produto?: ")
                        #o lower() serve para deixar letras maiusculas em minusculas, caso o usuario as digite em maiusculas
                        if certeza.lower() == "s" or certeza.lower() == "sim":
                            produtos[excluir]["estoque"] = "indisponivel"
                            print()
                            print(produtos)
                            print()
                            print("o produto foi confimado fora de estoque com sucesso!")
                            sair = input("aperte <enter> para sair: ")
                        else:
                            print("exclusão cancelada!")
                            sair = input("aperte <enter> para sair: ")
                else:
                    print("o codigo do produto não está cadastrado no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif not (decisao_produtos.isdigit()) or (decisao_produtos <= "0" or decisao_produtos > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")