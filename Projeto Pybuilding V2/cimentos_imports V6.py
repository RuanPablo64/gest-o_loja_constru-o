import pickle
import time
import datetime
import meus_arquivos
import funcoes_gerais
from funcoes_gerais import limpador
from funcoes_gerais import logo
from produtos import modulo_produtos
from clientes import modulo_clientes
from entregas import modulo_entregas
# um sistema de gestão para um loja de material de construção
# nome ficticio da loja: Cimentos Import's
#modulos: produtos, clientes, entregas
#Crud's: cadastrar, mostrar, atualizar e deletar
#atualizações: adicionei uma função para limpar o terminal (para não necessitar do uso de bibliotecas) e uma outra função para a logo do nome da loja aparecer em todas as ocasiões
#observação: estou focando em fazer o codigo funcional para na versão final polir o mesmo e deixar sua interface mais bonita
produtos = {
    # codigo chave (EAN/codigo de barras) : nome, preço, categoria do produto e em estoque (obs: a disponibilidade/ estoque do produto será importante para o modulo entregas)
    "11111111" : {
        "nome" : "cimento",
        "preço" : 4.5,
        "categoria" : "material bruto",
        "estoque" : "disponivel"

    },
    "22222222" : {
        "nome" : "ceramica",
        "preço" : 20.0,
        "categoria" : "piso",
        "estoque" : "disponivel"
    },
    "33333333" : {
        "nome" : "tijolo",
        "preço" : 2.0,
        "categoria" : "material bruto",
        "estoque" : "disponivel"
    }
}
clientes = {
    #codigo chave(senha de acesso) : nome, email, telefone
    "64646464" : {
        "nome" : "Ruan Pablo",
        "email" : "ruanP@gmail.com",
        "telefone" : "9610-0000",
        "aniversario" : "30/05/2008",
        "status" : "ativo"
    },
    "45454545" : {
        "nome" : "Julio Cesar",
        "email" : "JulioXd@gmail.com",
        "telefone" : "9701-0010",
        "aniversario" : "09/02/2007",
        "status" : "ativo"
    },
    "12121212" : {
        "nome" : "Mateus Batista",
        "email" : "mtb@gmail.com",
        "telefone" : "9411-0001",
        "aniversario" : "13/11/2007",
        "status" : "ativo"
    }
}
entregas = {
    #codigo chave(endereço por numero) : rua, EAN do produto para ser entregue, senha do cliente que registrou a entrega, data de entrega e entrega pendente ou feita
    "3245" : {
        "rua" : "rua da uf",
        "produto" : "11111111",
        "cliente" : "64646464",
        "data" : "10/07/2026",
        "pendencia" : "pendente"
    },
    "550" : {
        "rua" : "rua do if",
        "produto" : "33333333",
        "cliente" : "45454545",
        "data" : "31/07/2026",
        "pendencia" : "pendente"
    },
    "1002" : {
        "rua" : "rua do centro",
        "produto" : "22222222",
        "cliente" : "12121212",
        "data" : "12/06/2026",
        "pendencia" : "feita"
    }
}
produtos = meus_arquivos.ler_produtos()
clientes = meus_arquivos.ler_clientes()
entregas = meus_arquivos.ler_entregas()

decisao = "0"
while decisao != "6":
    limpador()
    logo()
    print()
    print()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+                           +")
    print("+        BEM - VINDO        +")
    print("+                           +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("#############################")
    print("#                           #")
    print("#                           #")
    print("#      1 - Produtos         #")
    print("#      2 - Clientes         #")
    print("#      3 - Entregas         #")
    print("#      4 - Relatorios       #")
    print("#      5 - Sobre o Sistema  #")
    print("#      6 - Sair do Progama  #")
    print("#                           #")
    print("#                           #")
    print("#############################")
    print("#############################")
    print()
    print()
    decisao = input("escolha uma das opções listadas: ")
    print()
    if decisao == "1":
        modulo_produtos(produtos)
    elif decisao == "2":
        modulo_clientes(clientes)
    elif decisao == "3":
        modulo_entregas(entregas, clientes, produtos)
    elif decisao == "4":
        decisao_relatorios = "0"
        while decisao_relatorios != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+     Relatorios da Loja    +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#    1 - Listagem Geral     #")
            print("#    2 - Filtro             #")
            print("#    3 - Processamento      #")
            print("#    4 - Combinação         #")
            print("#    5 - Sair do Modulo     #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_relatorios = input("escolha uma das opções listadas: ")
            if decisao_relatorios == "1":
                decisao_geral = "0"
                while decisao_geral != "4":
                    limpador()
                    logo()
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("+                           +")
                    print("+       Listagem Geral      +")
                    print("+                           +")
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("#############################")
                    print("#                           #")
                    print("#      1 - Produtos         #")
                    print("#      2 - Clientes         #")
                    print("#      3 - Entregas         #")
                    print("#      4 - Sair             #")
                    print("#                           #")
                    print("#############################")
                    print()
                    print()
                    decisao_geral = input("escolha uma das opções listadas: ")
                    print()
                    if decisao_geral == "1":
                        print(f"{"Codigo" :<13}{"Nome":<15}{"Preço":<10}{"Categoria":<20}{"Estoque":<10}")
                        print("-" * 70)
                        contador = 0
                        for ean, info in produtos.items():
                           print(f"{ean:<13}{info['nome']:<15}{info['preço']:<10}{info['categoria']:<20}{info['estoque']:<10}")
                           contador += 1
                        print()
                        print(f"existem {contador} produtos cadastrados no sistema")
                        sair = input("aperte <enter> para sair: ")
                    elif decisao_geral == "2":
                        print(f"{"Senha" :<13}{"Nome":<20}{"Email":<25}{"Telefone":<20}{"Aniversario":<20}{"Status":<10}")
                        print("-" * 120)
                        contador = 0
                        for senha, info in clientes.items():
                            print(f"{senha:<13}{info['nome']:<20}{info['email']:<25}{info['telefone']:<20}{info['aniversario']:<20}{info["status"]:<10}")
                            contador += 1
                        print()
                        print(f"existem {contador} clientes cadastrados no sistema")
                        sair = input("aperte <enter> para sair: ")   
                    elif decisao_geral == "3":
                        print(f"{"Endereço" :<13}{"Rua":<20}{"Produto":<25}{"Cliente":<20}{"Data":<20}{"Pendencia":<10}")
                        print("-" * 120)
                        contador = 0
                        for endereco, info in entregas.items():
                            print(f"{endereco:<13}{info['rua']:<20}{info['produto']:<25}{info['cliente']:<20}{info['data']:<20}{info['pendencia']:<10}")
                            contador += 1
                        print()
                        print(f"existem {contador} entregas cadastradas no sistema")
                        sair = input("aperte <enter> para sair: ")
                    else:
                        print()
                        print("você digitou uma opção invalida. tente novamente")
                        sair = input("aperte <enter> para voltar")
            elif decisao_relatorios == "2":
                decisao_filtro = "0"
                while decisao_filtro != "4":
                    limpador()
                    logo()
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("+                           +")
                    print("+    Listagem Com Filtro    +")
                    print("+                           +")
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("#############################")
                    print("#                           #")
                    print("#     1 - Por Categoria     #")
                    print("#     2 - Por Aniversario   #")
                    print("#     3 - Por Pendencia     #")
                    print("#     4 - Sair              #")
                    print("#                           #")
                    print("#############################")
                    print()
                    print()
                    decisao_filtro = input("escolha uma das opções listadas: ")
                    if decisao_filtro == "1":
                        busca_categoria = input("digite a categoria de produtos na qual deseja buscar: ")
                        print()
                        print(f"{"Codigo" :<13}{"Nome":<15}{"Preço":<10}{"Categoria":<20}{"Estoque":<10}")
                        print("-" * 70)
                        contador = 0
                        for ean, info in produtos.items():
                           if produtos[ean]["categoria"] == busca_categoria:
                            print(f"{ean:<13}{info['nome']:<15}{info['preço']:<10}{info['categoria']:<20}{info['estoque']:<10}")
                            contador += 1
                        print()
                        print(f"existe(m) {contador} produtos que pertencem a categoria de {busca_categoria}")
                        sair = input("aperte <enter> para sair: ")
                    elif decisao_filtro == "2":
                        busca_aniversario = input("digite o numero de algum mês do ano (mm): ")
                        print()
                        print(f"{"Senha" :<13}{"Nome":<20}{"Email":<25}{"Telefone":<20}{"Aniversario":<20}{"Status":<10}")
                        print("-" * 120)
                        contador = 0
                        for senha, info in clientes.items():
                            busca_mes = info["aniversario"].split("/")
                            if busca_mes[1] == busca_aniversario:
                                print(f"{senha:<13}{info['nome']:<20}{info['email']:<25}{info['telefone']:<20}{info['aniversario']:<20}{info["status"]:<10}")
                                contador += 1
                        print()
                        print(f"existe(m) {contador} clientes que fazem aniversario no mês {busca_aniversario}")
                        sair = input("aperte <enter> para sair: ")
                    elif decisao_filtro == "3":
                        busca_pendencia = input("digite se procura por entregas pendentes ou feitas [pendente(0)/feitas(1)]: ")
                        if busca_pendencia == "0":
                            print()
                            print(f"{"Endereço" :<13}{"Rua":<20}{"Produto":<25}{"Cliente":<20}{"Data":<20}{"Pendencia":<10}")
                            print("-" * 120)
                            contador = 0
                            for endereco, info in entregas.items():
                                if info['pendencia'] == "pendente":
                                    print(f"{endereco:<13}{info['rua']:<20}{info['produto']:<25}{info['cliente']:<20}{info['data']:<20}{info['pendencia']:<10}")
                                    contador += 1
                            print()
                            print(f"existe(m) {contador} entregas ainda pendentes")
                            sair = input("aperte <enter> para sair: ")
                        elif busca_pendencia == "1":
                            print()
                            print(f"{"Endereço" :<13}{"Rua":<20}{"Produto":<25}{"Cliente":<20}{"Data":<20}{"Pendencia":<10}")
                            print("-" * 120)
                            contador = 0
                            for endereco, info in entregas.items():
                                if info['pendencia'] == "feita":
                                    print(f"{endereco:<13}{info['rua']:<20}{info['produto']:<25}{info['cliente']:<20}{info['data']:<20}{info['pendencia']:<10}")
                                    contador += 1
                            print()
                            print(f"existe(m) {contador} entregas já feitas")
                            sair = input("aperte <enter> para sair: ")
                    else:
                        print("você digitou uma opção invalida. Tente novamente")
                        sair = input("aperte <enter> para voltar")
            elif decisao_relatorios == "3":
                decisao_processamento = "0"
                while decisao_processamento != "4":
                    limpador()
                    logo()
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("+                           +")
                    print("+       Listagem com        +")
                    print("+       Processamento       +")
                    print("+                           +")
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("#############################")
                    print("#                           #")
                    print("#     1 - Faixa de Preço    #")
                    print("#     2 - Faixa de Ano      #")
                    print("#     3 - Faixa de Data     #")
                    print("#     4 - Sair              #")
                    print("#                           #")
                    print("#############################")
                    print()
                    print()
                    decisao_processamento = input("digite uma das opções listadas: ")
                    if decisao_processamento == "1":
                        print()
                        faixa_inicial = input("digite uma faixa de preço inicial: ")
                        print()
                        faixa_final = input("digite uma faixa limite de preço: ")
                        print()
                        print(f"{"Codigo" :<13}{"Nome":<15}{"Preço":<10}{"Categoria":<20}{"Estoque":<10}")
                        print("-" * 70)
                        contador = 0
                        for ean, info in produtos.items():
                            if produtos[ean]["preço"] >= float(faixa_inicial) and produtos[ean]["preço"] <= float(faixa_final):
                                print(f"{ean:<13}{info['nome']:<15}{info['preço']:<10}{info['categoria']:<20}{info['estoque']:<10}")
                                contador += 1
                        print()
                        print(f"existe(m) {contador} produtos com essa faixa de preço")
                        sair = input("aperte enter para <voltar>")
                    elif decisao_processamento == "2":
                        print("")
    elif decisao == "5":
        limpador()
        logo()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("+                           +")
        print("+      Sobre o Sistema      +")
        print("+                           +")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("#############################")
        print("#                           #")
        print("#   sistema de gestão de    #")
        print("#       uma loja de         #")
        print("#   material de construção  #")
        print("#                           #")
        print("#      Desenvolvedor:       #")
        print("#        Ruan Pablo         #")
        print("#############################")
        print("#############################")
        print()
        print()
        sair = input("aperte <enter> para sair: ")
    elif not (decisao.isdigit()) or (decisao <= "0" or decisao > "6"):
        print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
        sair = input("aperte <enter> para voltar")
    
limpador()
print()    
print()
print()
print(''''                                                                                                                         
 mm    mm    mmmm    mm        mmmmmmmm  mmmmmmmm              mmmm    mmmmmmmm  mmm  mmm  mmmmmm    mmmmmm    mmmmmmmm 
 "##  ##"   ##""##   ##        """##"""  ##""""""            m#""""#   ##""""""  ###  ###  ##""""#m  ##""""##  ##"""""" 
  ##  ##   ##    ##  ##           ##     ##                  ##m       ##        ########  ##    ##  ##    ##  ##       
  ##  ##   ##    ##  ##           ##     #######              "####m   #######   ## ## ##  ######"   #######   #######  
   ####    ##    ##  ##           ##     ##                       "##  ##        ## "" ##  ##        ##  "##m  ##       
   ####     ##mm##   ##mmmmmm     ##     ##mmmmmm            #mmmmm#"  ##mmmmmm  ##    ##  ##        ##    ##  ##mmmmmm 
   """"      """"    """"""""     ""     """"""""             """""    """"""""  ""    ""  ""        ""    """ """""""" 
                                                                                                                        
                                                                                                                        ''')   
print()
print()
print("fim do progama")

#
meus_arquivos.grava_produtos(produtos)
meus_arquivos.grava_clientes(clientes)
meus_arquivos.grava_entregas(entregas)