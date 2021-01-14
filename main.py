#Funções
def aula ():#cria função
    print('aula de funções')

def naula ():
    print('aula x')

aula()#chama função
naula()

def cliente (nome):#função com parametro
    print('Ola, ',nome)

cliente("Mundo")#chama função com argumento

def entrada (user):
    print("obrigado ", user)

snome = input('Qual seu nome?')#entrada de dados

entrada(snome)#chama função com argumento recolhido da entrada

def soma (num1, num2):#função dinamica
    resultado = num1 + num2
    return resultado

print(soma(5,6))


