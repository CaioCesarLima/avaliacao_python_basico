produtos = []
total_vendas = []


def cadastrar_produto():
        produto = {}
        nome_produto = input("Escolha o nome do produto: ").lower()
        preco = float(input("Preço: "))
        estoque = int(input("Quantidade em estoque: "))
        produto["nome"] = nome_produto
        produto["preco"] = preco
        produto["estoque"] = estoque
        produtos.append(produto)
        print("Produto cadastrado!")


def calcular_total_venda(produto, quantidade):
    return produto["preco"] * quantidade


def vendas():
    print("Você escolheu realizar a venda")
    nome_produto = input("Qual produto deseja vender? ").lower()

    for produto in produtos:
        if produto["nome"] == nome_produto:
            if produto["estoque"] > 0:
                print(f"{nome_produto} está disponível para venda, e tem {produto['estoque']} unidade(s)")
                valor = int(input("Qual a quantidade deseja retirar ? "))

                if produto["estoque"] >= valor:
                    produto["estoque"] -= valor
                    total_venda = calcular_total_venda(produto, valor)

                  
                    total_vendas.append({
                        "produto": produto["nome"],
                        "quantidade": valor,
                        "total": total_venda
                    })

                    print(f"Venda realizada! Total: R$ {total_venda:.2f}")
                else:
                    print("Estoque insuficiente!")
            else:
                print("Produto sem estoque!")
            break
    else:
        print("Produto não encontrado.")


def listar_produtos():
  if produtos == [] :
    print(" Não há nenhum produto cadastrado.")
  else:
   for produto in produtos:
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")
        print("-" * 10)


def relatorio_vendas():
    if total_vendas == [] :
        print("Nenhuma venda foi realizada ainda.")
         
    print("\n Relatório de Vendas \n")
    total_itens = 0  
    total_ganho = 0

    for venda in total_vendas:
        print(f"Produto: {venda['produto']} "
              f"Quant.: {venda['quantidade']} "
              f"Total: R${venda['total']:.2f}")
        total_itens += venda["quantidade"]
        total_ganho += venda["total"]

    print(f"\nItens vendidos: {total_itens}")
    print(f"Total: R${total_ganho:.2f}\n")
  


while True:
    print( "=======Seja bem vindo a AssisTech=======")
    print("Digite 1 para Cadastrar produto ")
    print("Digite 2 para Realizar venda ")
    print("Digite 3 para Listar produtos ")
    print("Digite 4 para ver os Relatórios de venda ")
    print("Digite 5 para Sair do programa\n ")

    opcoes = int(input("Opção: "))

    if opcoes == 1 : 
     cadastrar_produto()

    elif opcoes == 2 : 
       vendas()

    elif opcoes == 3 : 
        listar_produtos()

    elif opcoes == 4 : 
        relatorio_vendas()

    elif opcoes == 5 : 
          print("=======Até a proxima.=======")
          break

    else :
            print("Valor invalido, favor escolher opção valida.")