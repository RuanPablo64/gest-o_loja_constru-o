import funcoes_gerais
from funcoes_gerais import logo
from funcoes_gerais import limpador
def modulo_clientes(clientes):
    decisao_clientes = "0"
    while decisao_clientes != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+      Modulo Clientes      +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#     1 - Criar Conta       #")
            print("#     2 - Ver Clientes      #")
            print("#     3 - Atualizar Usuario #")
            print("#     4 - Apagar Conta      #")
            print("#     5 - Sair do Modulo    #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_clientes = input("escolha uma das opções listadas: ")
            if decisao_clientes == "1":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Criação de Conta     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                print()
                senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
                funcoes_gerais.validar_senha(senha, clientes)
                print()
                nome = input("digite o nome do usuario: ")
                print()
                email = input("digite o email do usuario: ")
                while not funcoes_gerais.validar_email(email):
                    print("tente novamente")
                    email = input("digite o email do usuario: ")
                print()
                telefone = input("digite o numero de telefone do usuario: ")
                while not funcoes_gerais.validar_telefone(telefone):
                    print("tente novamente")
                    telefone = input("digite o numero de telefone do usuario: ")
                print()
                aniversario = input("digite o nascimento do usuario (DD/MM/AAAA): ")
                while not funcoes_gerais.validar_tempo_aniversario(aniversario):
                    print("tente novamente")
                    aniversario = input("digite o nascimento do usuario (DD/MM/AAAA): ")
                print()
                status = "ativo"
                clientes[senha] = {"nome" : nome, "email" : email, "telefone" : telefone, "aniversario" : aniversario, "status" : status}
                print(clientes)
                print()
                print("bem-vindo!")
                print("um novo cliente foi cadastrado no sistema")
                print()
                sair = input("aperte <enter> para sair: ")
            elif decisao_clientes == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Procurar Clientes    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                metodo = input("digite a maneira na qual deseja pesquisar o cliente [senha(1)/nome(2)]: ")
                if metodo == "1":
                    busca = input("digite a senha do usuario para busca: ")
                    if busca in clientes:
                        print(f"nome do cliente: {clientes[busca]["nome"]}")
                        print(f"email do cliente: {clientes[busca]["email"]}")
                        print(f"telefone do cliente: {clientes[busca]["telefone"]}")
                        print(f"aniversario do cliente: {clientes[busca]["aniversario"]}")
                        print(f"status do cliente: {clientes[busca]["status"]}")
                        print()
                        sair = input("aperte <enter> para sair: ")
                    else:
                        print("o cliente não está cadastrado no sistema")
                        sair = input("aperte <enter> para sair: ")
                elif metodo == "2":
                    busca_nome = input("digite o primeiro nome do cliente que deseja procurar: ")
                    contador = 0
                    for senha in clientes:
                        if clientes[senha]["nome"].startswith(busca_nome):
                            print(f"senha do cliente: {senha}")
                            print(f"email do cliente: {clientes[senha]["email"]}")
                            print(f"telefone do cliente: {clientes[senha]["telefone"]}")
                            print(f"aniversario do cliente: {clientes[senha]["aniversario"]}")
                            print(f"status do cliente: {clientes[senha]["status"]}")
                            print()
                            contador += 1
                    if contador == 0:
                        print("o nome do cliente informado não está cadastrado no sistema")
                        sair = input("aperte <enter> para sair")
                    else:
                        sair = input("aperte <enter> para sair")
                else:
                    print("você digitou uma opção invalida")
                    sair = input("aperte <enter> para sair")
            elif decisao_clientes == "3":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Atualização de       +")
                print("+          Usuario          +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                alteracao = input("digite a senha do usuario para atualização: ")
                if alteracao in clientes:
                    print(f"nome do cliente: {clientes[alteracao]["nome"]}")
                    print(f"email do cliente: {clientes[alteracao]["email"]}")
                    print(f"telefone do cliente: {clientes[alteracao]["telefone"]}")
                    print(f"aniversario do cliente: {clientes[alteracao]["aniversario"]}")
                    print(f"status do cliente: {clientes[alteracao]["status"]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    decisao_alteracao = "0"
                    while decisao_alteracao != "6":
                        limpador()
                        logo()
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("+                           +")
                        print("+       1 - Nome            +")
                        print("+       2 - Email           +")
                        print("+       3 - Telefone        +")
                        print("+       4 - Aniversario     +")
                        print("+       5 - Status          +")
                        print("+       6 - Sair            +")
                        print("+                           +")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
                        print()
                        if decisao_alteracao == "1":
                            limpador()
                            logo()
                            novo_nome = input("digite o novo nome do cliente: ")
                            while novo_nome == "":
                                print("você digitou um nome vazio. tente novamente")
                                novo_nome = input("digite o novo nome do cliente: ")
                            print()
                            clientes[alteracao]["nome"] = novo_nome
                            print(clientes)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "2":
                            limpador()
                            logo()
                            print()
                            email = input("digite o novo email do usuario: ")
                            while not funcoes_gerais.validar_email(email):
                                print("tente novamente")
                                email = input("digite o novo email do usuario: ")
                            print()
                            clientes[alteracao]["email"] = email
                            print()
                            print(clientes)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "3":
                            limpador()
                            logo()
                            print()
                            telefone = input("digite no novo telefone do usuario: ")
                            while not funcoes_gerais.validar_telefone(telefone):
                                print("tente novamente")
                                print()
                                telefone = input("digite no novo telefone do usuario: ")
                            print()
                            clientes[alteracao]["telefone"] = telefone
                            print()
                            print(clientes)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "4":
                            limpador()
                            logo()
                            print()
                            aniversario = input("digite a nova data de aniversario do usuario: ")
                            while not funcoes_gerais.validar_tempo_aniversario(aniversario):
                                print("tente novamente")
                                aniversario = input("digite a nova data de aniversario do usuario: ")
                            print()
                            clientes[alteracao]["aniversario"] = aniversario
                            print()
                            print(clientes)
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "5":
                            limpador()
                            logo()
                            print()
                            if clientes[alteracao]["status"] == "ativo":
                                print("o cliente ainda está ativo no sistema. Caso queira confirmar sua inatividade, acesse a área de exclusão desse modulo")
                                sair = input("aperte <enter> para voltar")
                            else:
                                mudanca = input("o cliente será considerado ativo novamente. tem certeza disso?: ")
                                if mudanca.lower() == "sim" or mudanca.lower() == "s":
                                    clientes[alteracao]["status"] == "ativo"
                                    print(clientes)
                                    print()
                                    print("o status do cliente foi alterado com sucesso")
                                    sair = input("aperte <enter> para voltar")
                                else:
                                    print("mudança cancelada!")
                                    sair = input("aperte <enter> para voltar")
                        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "6"):
                            print()
                            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
                            sair = input("aperte <enter> para voltar: ")
                else:
                    print("O cliente com status para ser alterado não está cadastrado no sistema")
                    print()
                    sair = input("aperte <enter> para sair: ")
            elif decisao_clientes == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Exclusão de Conta    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir = input("digite a senha de usuario para ser excluido: ")
                if excluir in clientes:
                    print()
                    print(f"nome do cliente: {clientes[excluir]["nome"]}")
                    print(f"email do cliente: {clientes[excluir]["email"]}")
                    print(f"telefone do cliente: {clientes[excluir]["telefone"]}")
                    print(f"aniversario do cliente: {clientes[excluir]["aniversario"]}")
                    print(f"status do cliente: {clientes[excluir]["status"]}")
                    print()
                    if clientes[excluir]["status"] == "inativo":
                        print("o cliente já se encontra inativo. Caso queira confirma-lo como ativo, acesse a área de atualizações desse modulo.")
                        sair = input("aperte <enter> para sair")
                    else:
                        certeza = input("você tem certeza de que deseja excluir esse cliente do sistema?: ")
                        if certeza.lower() == "s" or certeza.lower() == "sim":
                            clientes[excluir]["status"] = "inativo"
                            print()
                            print(clientes)
                            print()
                            print("o cliente foi registrado como inativo com sucesso!")
                            sair = input("aperte <enter> para sair: ")
                        else:
                            print("exclusão cancelada!")
                            sair = input("aperte <enter> para sair: ")
                else:
                    print("o cliente listado não possui cadastro no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif not (decisao_clientes.isdigit()) or (decisao_clientes <= "0" or decisao_clientes > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")