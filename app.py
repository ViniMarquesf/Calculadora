from Calculadora import Calculadora
calc = Calculadora()
 
n1 = float(input("digite o primeiro numero "))
n2 = float(input("digite o segundo numero "))
print("calculadora /n Somar, Subtrair, Multiplicar")

op=input("escreva o nome da operaçao desejada: ").lower()
 
if op == 'Somar':
    print(calc.soma(n1,n2))
elif op == 'Subtrair':
    print(calc.subtrair(n1,n2))
elif op == 'Multiplicar':
    print == (calc.multiplicar(n1,n2))

