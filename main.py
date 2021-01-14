"""
Método construtor é invocado quando a classe é instanciada, que é o nome dado
à ação de criar objeros a partir de uma classe
"""

class Retangulo:
    ladoA = None
    ladoB = None

    def __init__(self, ladoA, ladoB):#instanciando
        self.ladoA = ladoA
        self.ladoB = ladoB

"""
Herança é um mecanismo cujo objetivo é facilitar o reaproveitamento de código
"""

class pessoa:#classe mãe
    cidade = "padrão"
    UF = "padrão"
    bairro = "padrão"

    def estado(self):
        self.cidade = input("Qual a sua Cidade? ")
        self.UF = input("Pertence a qual UF? ")
        self.bairro = input("Você está em qual bairro? ")
        self.nome = input("OK! E qual seu nome? ")
        self.idade = input("qual sua idade? ")
        self.corCabelo = input("Se você tem cabelo, qual a cor? ")


class dadosPessoais(pessoa):
    nome = "padrão"
    idade = "padrão"
    corCabelo = "padrão"

user = dadosPessoais() #variavel recebe classe
user.estado()
print("OK! ", user.nome, "Você mora em ", user.cidade, ".", user.UF, "No bairro", user.bairro, "e tem ", user.idade, "anos.")

