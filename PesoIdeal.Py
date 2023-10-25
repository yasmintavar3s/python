altura = input('Qual é a sua altura em metros? ')
pesoatual = float(input('Qual é o seu peso atual?'))
genero= str(input('Responda F para gênero feminino e M para masculino: '))

alturarep=float(altura.replace(',','.'))
generoupper= genero.upper ()
pesoidealM= 72.7 *alturarep- 58
pesoidealF= 62.1*alturarep- 44.7


if generoupper =="F":
    print(f'Seu peso ideal é: {pesoidealF: .2F} kg')
elif generoupper =="M":
    print(f'Seu peso ideal é{pesoidealM: .2f} kg')
else:
   print(f'Opção inválida.Tente novamente escolhendo F ou M na questão sobre gênero.')
    

    

