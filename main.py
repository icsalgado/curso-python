#Estruturas de repetição
### WHILE ###
num = 0
while (num < 10):#parenteses não são obrigatórios
    print("Numero atual ", num)
    num = num + 1 #incremento para evitar loop infinito
### FOR ###
print("tabuada")
for i in range(10):#conta 10 repetições
    for j in range(10):
        print(i, " x ", j, "|", i*j)
    print("__________________")
