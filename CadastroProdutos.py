
estoque=0
resp="s"
nome=0
preco=0
quant=0


while resp =="s" or resp =="S":
    nome=str(input("Digite o nome do produto: "))
    preco= float(input("Digite o preço: "))
    quant=int(input("Digite a quantidade: "))
    
    print("Nome\t\t\t\tPreço\t\t\t\tQuantidade")
    print("-------------------------------------------------------------------------------------")
    print(f'{nome}\t\t\t{preco}\t\t\t\t\t{quant}')
    print("-------------------------------------------------------------------------------------")
    precototal= preco*quant
    print(f'Total:\t\t\t\t{precototal}\t\t\t\t')
    resp=str(input("Digite S se deseja continuar cadastrando e N se deseja parar:"))


