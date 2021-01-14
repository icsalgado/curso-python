def criarArquivo():
    arquivo = open("dados.txt","w")#w abre
    arquivo.close()
    print("txt criado")

def escreveArquivo():
    nome = input("seu nome: ")
    arquivo = open("dados.txt","a")#a altera, escreve
    arquivo.write(nome)
    arquivo.close()

def lerArquivo():
    arquivo = open("dados.txt", "r")#r ler
    line = arquivo.readline()
    while line != "":
        print(line)
        line = arquivo.readline()
    arquivo.close()

criarArquivo()
escreveArquivo()
lerArquivo()