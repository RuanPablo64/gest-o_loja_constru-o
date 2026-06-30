import funcoes_gerais
from funcoes_gerais import logo
from funcoes_gerais import limpador
def excluir_produto(produtos):
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



def excluir_cliente(clientes):
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


def excluir_entrega(entregas):
    excluir = input("digite o endereço de entrega na qual deseja confirmar a realização da mesma: ")
    if excluir in entregas:
        print()
        print(f"rua da entrega: {entregas[excluir]["rua"]}")
        print(f"nome do produto a ser entregue: {entregas[excluir]["produto"]}")
        print(f"nome do cliente: {entregas[excluir]["cliente"]}")
        print(f"data de entrega: {entregas[excluir]["data"]}")
        print(f"pendencia: {entregas[excluir]["pendencia"]}")
        print()
        if not funcoes_gerais.validar_pendencia(excluir, entregas):
            sair = input("aperte <enter> para sair")
        else:
            certeza = input("você tem certeza de que deseja atualizar a entrega como feita?: ")
            if certeza.lower() == "s" or certeza.lower() == "sim":
                entregas[excluir]["pendencia"] = "feita"
                print()
                print(entregas)
                print()
                print("a entrega foi realizada com sucesso!")
                sair = input("aperte <enter> para sair: ")
            else:
                print("exclusão cancelada!")
                sair = input("aperte <enter> para sair: ")
    else:
        print("a entrega listada não está cadastrada no sistema")
        sair = input("aperte <enter> para sair: ")
