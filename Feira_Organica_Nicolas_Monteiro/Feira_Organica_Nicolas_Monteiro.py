import os


cadastro = []
pag = ['0- Crédito','1- Débito','2- Dinheiro']
ficha = []
titulos = (
    '§ Folhas e Hortaliças §',
    '§ Frutas §',
    '§ Raízes, tubérculos, legumes e afins §',
    '§ Outros §',
    '§ Pastinhas, astepasto e geleias §',
    '§ Lanches (sem trigo) §',
    '§ Lanches (com trigo) §'
)
produtos = [
    [('Alface americano = ', 2.50),( 'Alface crespa = ', 2.50),( 'Alho poró = ', 2.00), ('Capim santo = ', 2.50),( 'Cebola = ', 3.00),( 'Cebolinha = ', 2.50), ('Coentro = ', 2.50), ( 'Couve folha = ', 2.50), ('Chinguezay (acelga chinesa) = ', 3.00), ('Espinafre = ', 3.00), ('Hortelã = ', 2.50), ('Salsinha = ', 2.50), ('Rúcula = ', 2.50)],
    [('Banana pacovan (unidade) = ', 0.25), ('Cana(saquinho) = ', 2.00),('Laranja comum (4 Unidades) = ', 2.00), ('Laranja mimo (4 Unidades) = ', 2.00), ('Maracujá (kg) = ', 7.00)],
    [('Batata doce (kg) =', 4.00), ('Cará (kg) =', 5.00),( 'Cenoura(molho) = ', 3.00),('Jerimum (kg) = ', 5.00), ('Macaxeira (kg)', 4.00), ('Rabanete(molho)', 2.50), ('Quiabo (15 Un)', 2.00)],
    [('Fava seca (Kg) =', 12.00),( 'Mel italiana (250 g) =', 20.00),( 'Mel italiana (500 g) =', 35.00), ('Mel no favo (450 g) =', 25.00),( 'Ovos de capoeira (un) =', 1.00),( 'Polpa de cajá (400g) =', 6.00), ('Própolis (20 ml) =', 16.00), ('Pão sem trigo (grande) =', 13.00), ('Pão com trigo (grande) =', 13.00), ('Pão com trigo (pequeno) =', 7.00),( 'Bolo(sem trigo) =', 10.00),( 'Bolinho de bacia(c/trigo) =', 2.00), ('Mini pizza (un) =', 3.00),( 'Pizza brotinho =', 5.00),( 'Bolacha com trigo (saquinho) =', 5.00),( 'Sucos sem açucar (200 ml) =', 3.00),( 'Sucos com açucar (200 ml) =', 3.00),('Sucos com ou sem açucar (1 l) =', 10.00),( 'Refeições congeladas (500 g) =', 12.00), ('Refeições congeladas (750 g) =', 15.00), ('Hambúrguer de ora-pro-nóbis, (6 Un) =', 12.00),( 'Molhos prontos =', 10.00),( 'Massa artesanal (lasanha ou taglatelle) =', 12.00)],
    [('Pepita de girassol', 5.00), ('Homus de grão de bico com paprika', 5.00),('Bisnaga Maionese de pepita de girassol (250 ml)', 10.00), ('Pimentas ao mel de engenho', 15.00), ('Confit de tomatinho, pimenta, pimentão ou berinjela', 15.00), ('Geleia de tomate com pimenta/abacaxi/manga', 13.00),('Capotana Siciliana', 13.00)],
    [('Quiche de macaxeira c/ alho poró', 5.00), ('Quiche de macaxeira c/ tomate seco', 5.00), ('Sanduíche sem glúten de ricota', 6.00), ('Sanduíche sem glúten de caponata Siciliana', 6.00), ('Sanduíche sem glúten de ragu', 6.00)],
    [('Empada de falso camarão', 5.00), ('Empada de antepasto de berinjela', 5.00), ('Empada de tofu com cebola caramelizada', 5.00), ('Pãozinhos de inhames recheados', 5.00)],
]
setores = {'0' :'Folhas e Hortaliças', '1': 'Frutas', '2': 'Raízes,Tubérculos e afins', '3': 'Outros',
           '4': 'Pastinhas, antepastos e geleias', '5': 'Lanches sem trigo', '6': 'Lanches com trigo'}

def pagamento():
    paga = -1
    for p in pag:
        print (p)
    while paga < 0 or paga > 2:
        paga = int(input('Escolha a forma de pagamento: '))
    ficha.append('Forma de pagamento:')
    ficha.append(pag[paga])

def adicionar():
    cadastro.append('Quantidade:')
    cadastro.append(quant)
    cadastro.append('Preço: R$')
    cadastro.append(preco)

def secao(id):
    cont = 0
    print()
    for f in range(0,len(produtos[id])):
        print(cont,produtos[id][f])
        cont += 1
    print('')

total = 0
print('')
print('Seja bem vindo a Feira Orgânica do Supermercados Medlin:')
while True:
    rod = 0
    ir = -1
    pedido = -1
    quant = 0
    print('§-'*30)
    print('\t    Escolha o setor que deseja conferir:')
    print('§-'*30)
    for n, s in setores.items():
            print(n, '-', s)
    print('§-'*30)
    rod += 1        
    while ir < 0 or ir > 6:
        ir = int(input('Escolha o código do setor: '))
    secao(ir)
    while pedido < 0 or pedido > len(produtos[ir]) - 1:
        pedido = int(input('Informe item de preferência: '))
    while quant < 1:
        quant = int(input(f'Quantidade do item : '))
    preco = (produtos[ir][pedido][1]) * quant
    total += preco
    cadastro.append('Pedido:')
    cadastro.append(produtos[ir][pedido][0])
    adicionar()
    print('Carrinho:',total)

    sair = input('Deseja finalizar a compra?(s/n)' )
    os.system('cls' if os.name == 'nt' else 'cls')
    if sair == 's':
        cadastro.append('Total - R$')
        cadastro.append(total)
        print('Vamos fazer seu cadastro:')
        nome = input('Informe seu nome: ')
        ficha.append('Nome:')
        ficha.append(nome)
        end = input('Informe seu endereço: ')
        ficha.append('Endereço:')
        ficha.append(end)
        pagamento()
        print('§-Cupom fiscal-§')
        for c in cadastro:
            print(c)
        for f in ficha:
            print(f)
        cliente = str(ficha)
        pedido = str(cadastro)
        
    
        
        #Coloquei o 'w', mas se desejar mudar para 'x' para criar o arquivo e depois 'w' novamente, alternativa para criar arquivo, mas estará anexado, por vias das dúvidas.      
        with open('dadospedido.txt', 'w',encoding='utf8') as arquivo:
            arquivo.write('Cupom fiscal:\n')
            arquivo.writelines(cliente)
            arquivo.write('\n')
            arquivo.writelines(pedido)
            break