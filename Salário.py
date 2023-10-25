def salliquido(salhora,horas,descontos):
    salliquido = (salhora*horas) - descontos
    print(f'O salário líquido é: R${salliquido:.2f}')

salhora =(float(input("Digite o salário: ")))
horas =(float(input("Digite as horas trabalhadas: ")))
descontos =(float(input("Digite os descontos: ")))

total=salliquido(salhora,horas,descontos)

