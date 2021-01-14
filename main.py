#Listas utilizam colchetes e tuplas utilizam parenteses

lista = ["Daniel", "Leticia", "Fernando", "Maria"]
lista2 = [10,20,30,40]

soma = lista + lista2 #independente do tipo de variavel

print(lista)
print(lista[2])
print(lista2)
print(soma)

for elemento in soma:#exibe em lista vertical
    print(elemento)

if("Daniel" in soma):#busca detalhada
    print("contém")
else:
    print("não contém")