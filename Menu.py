def soma(n1,n2):
    soma=n1+n2
    print(f"O resultado da operação é: {soma}")
def subtracao(n1,n2):
    subtracao=n1-n2
    print(f"O resultado da operação é: {subtracao}")
def multiplicacao(n1,n2):
    multip=n1*n2
    print(f"O resultado da operação é: {multip}")
def divisao(n1,n2):
    div=n1/n2
    print(f"O resultado da operação é: {div}")

n1=int(input("Digite o 1° número: "))
n2= int(input("Digite o 2° número: "))

op=int(input("Operações:\n" "1-Soma \n""2-Subtração \n""3-Multiplicação\n""4-Divisão\n""9-Sair do programan\n""Ditite o número correspondente à operação que deseja realizar:"))

if op ==1:
    total= soma(n1,n2)
elif op==2:
    total=subtracao(n1,n2)
elif op==3:
    total=multiplicacao(n1,n2)
elif op==4:
    total=divisao(n1,n2)
elif op==9:
    print("Fim do programa")
else:
    print("Código inválido")