import time

# Array de Produtos
produtos = []
vendas = []


# Cadastrar produtos
def add_produto():
  nome_value = str(input("Preencha o nome do produto: \n\n"))
  preco_value = float(input("Preencha o preço do produto: \n\n"))
  quantidade_value = int(input("Preencha a quantidade do produto em estoque: \n\n"))
  produto = {
         "nome": nome_value,
         "preco": preco_value,
         "quantidade": quantidade_value
  }
  produtos.append(produto)
  print("Produto Adicionado com sucesso")



# Listar Produtos 
def listar_produtos():
  for produto in produtos:
   print(produto)

  


# Realizar Venda
def realizar_venda():
    nome_produto = str(input("Digite o nome do produto que deseja vender: \n\n"))
    quantidade_venda = int(input("Digite a quantidade a vender: \n\n"))

    for produto in produtos:
        if produto["nome"] == nome_produto:
            if produto["quantidade"] >= quantidade_venda:
                produto["quantidade"] -= quantidade_venda
                total = quantidade_venda * produto["preco"]
                vendas.append({
                    "nome": produto["nome"],
                    "quantidade": quantidade_venda,
                    "total": total
                })
            else:
                 print("Estoque insuficiente")


# Listar vendas
def listar_vendas():
  for venda in vendas:
   print(venda)


opcoes = 0

while opcoes != 5:
    print("---------------- Menu ----------------")

    print("1. Cadastrar produto: ")
    print("2. Realizar venda: ")
    print("3. Listar Produtos: ")
    print("4. Relario de vendas: ")
    print("5. Sair do sistema: ")

    print("--------------------------------------")
    opcoes = int(input("Escolha uma função\n\n"))

    # Cadastrar produtos
    if opcoes == 1:
            print("--------------------------------------")
            add_produto()
            listar_produtos()
            print("--------------------------------------")
            time.sleep(5)



    # Realizar Vendas       
    elif opcoes == 2:
            print("--------------------------------------")
            realizar_venda()
            print("--------------------------------------")
            time.sleep(5)        



    # Listar Produtos               
    elif opcoes == 3:
            print("--------------------------------------")
            print("Produtos disponiveis: ")
            listar_produtos()
            
            print("--------------------------------------")
            time.sleep(5)              



    # Relatorio de vendas                     
    elif opcoes == 4:
            print("--------------------------------------")
            listar_vendas()
            print("--------------------------------------")
            time.sleep(5)              



    # Encerrar programa                      
    else :
            print("--------------------------------------")
            print("Encerrando o programa")
            print("--------------------------------------")
            break