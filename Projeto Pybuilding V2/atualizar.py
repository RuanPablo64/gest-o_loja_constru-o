from funcoes_gerais import logo
from funcoes_gerais import limpador
import funcoes_gerais

def atualizar_clientes(clientes, alteracao):
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


def atualizar_produtos(produtos, alteracao):
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
            produtos[alteracao]["nome"] = nome.lower()
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
            produtos[alteracao]["preço"] = float(preco)
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
            produtos[alteracao]["categoria"] = nova_categoria.lower()
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

def atualizar_entregas(entregas, produtos, clientes, alteracao):
    decisao_alteracao = "0"
    while decisao_alteracao != "6":
        limpador()
        logo()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("+                           +")
        print("+       1 - Rua             +")
        print("+       2 - Produto         +")
        print("+       3 - Cliente         +")
        print("+       4 - Data            +")
        print("+       5 - Pendencia       +")
        print("+       6 - Sair            +")
        print("+                           +")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
        print()
        if decisao_alteracao == "1":
            nova_rua = input("digite o nome da nova rua de entrega do pedido: ")
            if nova_rua == "":
                print("você digitou uma rua vazia. tente novamente")
                nova_rua = input("digite o nome da nova rua de entrega do pedido: ")
            else:
                print()
                entregas[alteracao]["rua"] = nova_rua
                print(entregas)
                print()
                print("o status da entrega foi atualizada com sucesso")
                sair = input("aperte <enter> para voltar: ")
        elif decisao_alteracao == "2":
            print()
            novo_ean_produto = input("informe o codigo do novo produto a ser entregue: ")
            if novo_ean_produto not in produtos or produtos[novo_ean_produto]["estoque"] != "disponivel":
                if novo_ean_produto not in produtos:
                    print("o produto solicitado não está cadastrado no sistema")
                    sair = input("aperte <enter> para voltar")
                elif produtos[novo_ean_produto]["estoque"] != 2:
                    print("o produto solicitado não está em estoque/disponivel no momento")
                    sair = input("aperte <enter> para voltar: ")
            else:
                print()
                entregas[alteracao]["produto"] = produtos[novo_ean_produto]["nome"]
                print(entregas)
                print()
                print("o status da entrega foi atualizado com sucesso")
                sair = input("aperte <enter> para voltar")
        elif decisao_alteracao == "3":
            print()
            nova_senha_cliente = input("digite a senha do novo cliente que solicitou a entrega: ")
            if nova_senha_cliente not in clientes:
                print()
                print("a senha do cliente solicitado não está registrado no sistema")
                sair = input("aperte <enter> para voltar: ")
            else:
                entregas[alteracao]["cliente"] = clientes[nova_senha_cliente]["nome"]
                print()
                print(entregas)
                print()
                print("o status da entrega foi atualizado com sucesso")
                sair = input("aperte <enter> para voltar")
        elif decisao_alteracao == "4":
            print()
            data_entrega = input("digite a nova data de entrega do pedido: ")
            while not funcoes_gerais.validar_data_entrega(data_entrega):
                print("tente novamente")
                data_entrega = input("digite a nova data de entrega do pedido: ")
            print()
            entregas[alteracao]["data"] = data_entrega
            print(entregas)
            print()
            print("o status da entrega foi atualizado com sucesso")
            sair = input("aperte <enter> para voltar")
        elif decisao_alteracao == "5":
            print()
            if entregas[alteracao]["pendencia"] == "pendente":
                print("a entrega ainda está pendente. Caso queira confirmar que a entrega foi finalizada, acesse a área de cancelamente de pendencia desse modulo")
                sair = input("aperte <enter> para voltar")
            else:
                mudanca = input("tem certeza de que deseja confirmar essa entrega como pendente?")
                if mudanca.lower() == "s" or mudanca.lower() == "sim":
                    print()
                    entregas[alteracao]["pendencia"] == "pendente"
                    print(entregas)
                    print()
                    print("o status da entrega foi atualizado com sucesso")
                    sair = input("aperte <enter> para voltar")
                else:
                    print("mudança cancelada!")
                    sair = input("aperte <enter> para voltar")
        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "6   "):
            print()
            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
            sair = input("aperte <enter> para voltar: ")