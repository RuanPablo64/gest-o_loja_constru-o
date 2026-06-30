import funcoes_gerais
from funcoes_gerais import logo
from funcoes_gerais import limpador
from cadastro import cadastrar_entrega
from procurar import procurar_entregas
from atualizar import atualizar_entregas
from excluir import excluir_entrega
def modulo_entregas(entregas, clientes, produtos):
    decisao_entrega = "0"
    while decisao_entrega != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+      Modulo Entregas      +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#    1 - Registar Entrega   #")
            print("#    2 - Ver Entregas       #")
            print("#    3 - Status da Entrega  #")
            print("#    4 - Cancelar Pendencia #")
            print("#    5 - Sair do Modulo     #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_entrega = input("escolha uma das opções listadas: ")
            if decisao_entrega == "1":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+     Registrar Entrega     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                cadastrar_entrega(entregas, clientes, produtos)
            elif decisao_entrega == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+   Procurar Por Entregas   +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                procurar_entregas(entregas)
            elif decisao_entrega == "3":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Status de Entrega    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                #aqui também se encontra a mesma ideia de que caso o cliente ou produto não esteja cadastrado, a entrega não é atualizada
                alteracao = input("digite o endereçço de entrega: ")
                if alteracao in entregas:
                    print(f"rua de entrega: {entregas[alteracao]["rua"]}")
                    print(f"nome do produto: {entregas[alteracao]["produto"]}")
                    print(f"nome do cliente: {entregas[alteracao]["cliente"]}")
                    print(f"data de entrega: {entregas[alteracao]["data"]}")
                    print(f"pendencia: {entregas[alteracao]["pendencia"]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    atualizar_entregas(entregas, clientes, produtos, alteracao)
                else:
                    print("a rua informada não foi encontrada no sistema")
                    sair = input("aperte <enter> para sair")
            elif decisao_entrega == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Cancelar Pendencia   +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir_entrega(entregas)
            elif not (decisao_entrega.isdigit()) or (decisao_entrega <= "0" or decisao_entrega > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")