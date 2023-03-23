import time

print('Bem vindo ao Supermercado online!')
itens=['Maçã','Uva','Banana']
itens_lista=[]
preços=[2.99,1.99,4.99]
soma=0
time.sleep(2)
print('''
itens disponíveis: 
---------------''')
print(','.join(itens))
print('---------------')

time.sleep(1.3)

while True:
    item = input("Digite o item que você quer adicionar ao carrinho: ")
    if item in itens:
        itens_lista.append(item)
        itens.remove(item)
        print('Seu carrinho: ')
        print('-'.join(itens_lista))
    else:
        print('Esse item não existe')

    parar=input('Deseja adicionar mais itens? ')
    if parar=='n' or parar=='nao' or parar== 'não':
        break

while True:
    remover = input("deseja remover algum item? ")
    if remover== 's' or remover=='sim':
        remover_item=input('Qual item você deseja remover? ')
        if remover_item in itens_lista:
            itens_lista.remove(remover_item)
            print('Seu carrinho: ')
            print('-'.join(itens_lista))
        else:
            print('Este item não está no carrinho.')
    else:
        time.sleep(1.3)
        print('Carrinho salvo')
        break

time.sleep(1.3)
total = sum([preços[itens.index(item)] for item in itens_lista])
print("Seu carrinho:")
for item in itens_lista:
    print("- " + item)
print("Total da compra: R$ %.2f" % total)
