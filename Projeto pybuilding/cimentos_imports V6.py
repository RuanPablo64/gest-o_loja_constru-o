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
        "preço" : "4,5",
        "categoria" : "material bruto",
        "estoque" : "disponivel"

    },
    "22222222" : {
        "nome" : "ceramica",
        "preço" : "20,0",
        "categoria" : "piso",
        "estoque" : "disponivel"
    },
    "33333333" : {
        "nome" : "tijolo",
        "preço" : "2,0",
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
    #codigo chave(endereço) : nome do produto para ser entregue, nome do cliente que registrou a entrega, data de entrega e entrega pendente ou feita
    "rua da uf" : {
        "produto" : "cimento",
        "cliente" : "Ruan Pablo",
        "data" : "10/07/2026",
        "pendencia" : "pendente"
    },
    "rua do if" : {
        "produto" : "tijolo",
        "cliente" : "Julio Cesar",
        "data" : "31/07/2026",
        "pendencia" : "pendente"
    },
    "rua do centro" : {
        "produto" : "ceramica",
        "cliente" : "Mateus Batista",
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
        while decisao_relatorios != "4":
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
            print("#   1 - Listagem Geral      #")
            print("#   2 - Listagem com Filtro #")
            print("#   3 - Sobre as Entregas   #")
            print("#   4 - Sair do modulo      #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_relatorios = input("escolha uma das opções listadas: ")
            if decisao_relatorios == "1":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
                sair = input("aperte <enter> para voltar")
            elif decisao_relatorios == "2":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
                sair = input("aperte <enter> para voltar")
            elif decisao_relatorios == "3":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
                sair = input("aperte <enter> para voltar")
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