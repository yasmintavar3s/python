vetor=[]
resp="s"


while resp=="s" or resp=="S":
    n1= int(input("Digite um número: "))
    vetor.append(n1)
    print(f'Seu conjunto de números é {vetor}')
    resp= str(input("Se deseja continuar digite S ou N se deseja mostrar os resultados: "))

soma= sum(vetor)
quant= len(vetor)
media= soma/quant 


print(f'A soma dos itens é {soma}, a média é {media} e a quantidade de itens é {quant}')




