#Variáveis, operadores aritméticos/relacionais/lógicos, if/else
#Estruturas de repetição

### variáveis ###
inteiros = 2021
reais = 2.46
booleanos = True
frase = "curso Python"

#saida de dados
print(inteiros, reais, frase)#virgulas concatenam

### Operadores aritméticos ###
x = 10
y  = 5
soma = x+y
sub = x-y
div = x/y
div2 = y/x
mult = x*y
exp = x**y
print(soma, sub, div, div2, mult, exp)

### Operadores relacionais/lógicos if/else ###
var1 = 15
var2 = 10
if (var1 > var2):#dois pontos é como um imperativo faça!
    print(var1, " > ", var2)
    if(var1 + var2 >= 100):
        print("maior que 100")
    else:
        if(var1 + var2 != 25):
            print("diferente de 25")
        else:
            if var1 + var2 == 25:#parenteses não são obrigatórios
                print("soma é igual a ", var1+var2)
            else:
                print("encadeados")
if var1-var2 and var2-var1 > 0:
    print("AND")
elif var1-var2 or var2-var1 > 0:
    print("OR")