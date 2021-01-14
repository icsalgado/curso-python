#tuplas
tupla = (25, 26.9, "Fulano")
indice = 0
while (indice < len(tupla)):
    print(tupla[indice])
    indice = indice+1

numeros = (1, 2, 3, 4, 5, 'numero')
for sequencia in numeros:
    print(sequencia)

sec1 = (1, 2, 3, 4, 5, 6, 7)
sec2 = sec1[0:5]#posição inicial concatena posição final
print(sec2)

nome = "Fulano Fulaninho de Tal"
print (nome[0:8])#cordas strings