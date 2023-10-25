resp='s'
total=0

while resp == 'S' or resp =='s': 
    cod =int(input('Digite o código do lanche que deseja pedir: '))
    quant =int(input('Digite a quantidade desejada:'))

    if cod == 100:
        total=total + 1.20 * quant
    elif cod == 101:
        total=total + 1.30 * quant
    elif cod == 102:
        total=total + 1.50 * quant
    elif cod == 103:
        total=total + 1.20 * quant
    elif cod == 105:
        total= total + 1.00 * quant
    else:
        print("Código inválido")
   
    
    
    print(f'O total da sua compra é R$ {total:.2f}')
    resp = str(input('Digite S se deseja continuar comprando ou N se prefere parar: '))

print('Obrigada pelo pedido, até a próxima!')
