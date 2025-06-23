carrinho_de_compras = {

}


def adicionar_item(produto: str, quantidade: int): #ele pode criar o produto e add a quantidade
    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return
    if produto in carrinho_de_compras:
        carrinho_de_compras[produto] += quantidade
        print(f"{quantidade} unidade(s) adicionada(s) a {produto}.")
    else:
        carrinho_de_compras[produto] = quantidade
        print(f"{produto} adicionado ao carrinho com {quantidade} unidade(s).")

def remover_item(produto: str, quantidade: int):
    if produto in carrinho_de_compras:
        del carrinho_de_compras[produto]
        print(f'O {produto} foi removido do carrinho de compras')
    else:
        print('Ele não estava no carrinho de compras, não há nada para remover')
    return produto

def atualizar_quant(produto: str, quantidade: int):
    if produto not in carrinho_de_compras:
        print("Este item não está no carrinho.")
        return
    if quantidade > 0:
        carrinho_de_compras[produto] = quantidade
        print(f"A quantidade de {produto} foi atualizada para {quantidade}.")
    else:
        remover_item(produto)  
        print(f"{produto} foi removido do carrinho porque a quantidade foi menor ou igual a zero.")

def visualizar_itens(): #não precisa dos parametros, apenas do carrinho inteiro
    if not carrinho_de_compras:
        print("O carrinho de compras está vazio.")
    else:
        print("Itens no carrinho:")
        for produto, quantidade in carrinho_de_compras.items():
            print(f'Produto: {produto}, Quantidade: {quantidade}')
        total = sum(carrinho_de_compras.values()) #mostra o total de quantidades, valores
        print(f"Quantidade total de itens: {total}")
    return


def limpar_carrinho(): #não precisa dos parametros, apenas do carrinho inteiro
    if carrinho_de_compras:
        carrinho_de_compras.clear()
        print("O carrinho de compras foi esvaziado.")
    else:
        print("O carrinho de compras está vazio, não há nada para limpar.")

def menu():
    continuar = True
    while continuar:
        escolha = input('Digite 2 se quiser adicionar item:\n' \
        'Digite 3 se quiser remover item:\n' \
        'Digite 4 se quiser atualizar quantidade:\n' \
        'Digite 5 se quiser visualizar item:\n' \
        'Digite 6 se quiser limpar o carrinho:\n' \
        'Digite 1 para continuar ou qualquer para encerrar:\n')

        if escolha == '2':
            produto = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar_item(produto, quantidade)

        elif escolha == '3':
            produto = input("Nome do produto a remover: ")
            quantidade = input("Quantidade:")
            remover_item(produto, quantidade)

        elif escolha == '4':
            produto = input("Nome do produto: ")
            quantidade = int(input("Nova quantidade: "))
            atualizar_quant(produto, quantidade)

        elif escolha == '5':
            visualizar_itens()

        elif escolha == '6':
            limpar_carrinho()

        elif escolha == '1':
            print("Encerrado. Aproveite as compras")
            continuar = False

print(menu())