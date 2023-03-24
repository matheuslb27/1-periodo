import time

print('Bem vindo ao Supermercado online!')
itens=['Maçã','Uva','Banana']
itens_lista=[]
preço=[2.99,1.99,4.99]
time.sleep(2)

print('''
itens disponíveis: 
---------------''')
print(','.join(itens))
print('---------------')

time.sleep(1.3)

while True:
    item = input("Digite o item que você quer adicionar ao carrinho : ")
    if item not in itens:
        print('Esse item não existe')
        continue
    itens_lista.append(item)
    parar=input('Deseja adicionar mais itens? ')
    if parar in ['n', 'nao', 'não']:
        break
    
print('Seu carrinho: ')
for item in itens_lista:
    print("- " + item)

while True:
    remover = input("deseja remover algum item? ")
    if remover in ['s', 'sim']:
        remover_item=input('Qual item você deseja remover? ')
        if remover_item in itens_lista:
            itens_lista.remove(remover_item)
        else:
            print('Esse item não está no carrinho')
        print("Seu carrinho: ")
        print("\n".join("- " + item for item in itens_lista))

    else:
        time.sleep(1.3)
        print('Carrinho salvo')
        break

total = sum(preço[itens.index(item)] for item in itens_lista)
for item in itens_lista:
    print("- " + item)
print("Total da compra: R$ %.2f" % total)
