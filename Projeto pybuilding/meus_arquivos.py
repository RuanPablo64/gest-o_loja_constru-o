import pickle
def ler_produtos():
    try:
        produtos = {}
        arqprodutos = open("produtos.dat", "rb")
        produtos = pickle.load(arqprodutos)
        arqprodutos.close()
    except:
        produtos = {
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
        arqprodutos = open("produtos.dat", "wb")
        pickle.dump(produtos, arqprodutos)
        arqprodutos.close()
    return produtos

def ler_clientes():
    try:
        clientes = {}
        arqclientes = open("clientes.dat", "rb")
        clientes = pickle.load(arqclientes)
        arqclientes.close()
    except:
        clientes = {
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
        arqclientes = open("clientes.dat", "wb")
        pickle.dump(clientes, arqclientes)
        arqclientes.close()
    return clientes
def ler_entregas():
    try:
        entregas = {}
        arqentregas = open("entregas.dat", "rb")
        entregas = pickle.load(arqentregas)
        arqentregas.close()
    except:
        entregas = {
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
        arqentregas = open("entregas.dat", "wb")
        pickle.dump(entregas, arqentregas)
        arqentregas.close()
    return entregas
def grava_produtos(produtos):
    arqprodutos = open("produtos.dat", "wb")
    pickle.dump(produtos, arqprodutos)
    arqprodutos.close()
def grava_clientes(clientes):
    arqclientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arqclientes)
    arqclientes.close()
def grava_entregas(entregas):
    arqentregas = open("entregas.dat", "wb")
    pickle.dump(entregas, arqentregas)
    arqentregas.close()
    
