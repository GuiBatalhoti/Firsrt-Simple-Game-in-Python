# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os

# Board (tabuleiro)
tela = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', ''' 

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classes

class Forca():

    def __init__(self):
        self.letras_corretas = []
        self.letras_erradas = []
        self.palavra_escondida = []
        self.BuscaPalavra()

    def BuscaPalavra(self):
        file = open("palavras.txt", "r", encoding="utf8")
        linha = file.readlines()
        self.palavra = linha[random.randint(0, len(linha) - 1)]
        for _ in range(len(self.palavra) - 1):
            self.palavra_escondida.append("_")

    def ImprimeJogo(self):
        print(tela[len(self.letras_erradas)])
        print("Palavra: ", end="")
        for i in self.palavra_escondida:
            print(i, end="")
        print("\nErros: ")
        for i in self.letras_erradas:
            print(i + " ",end="")
        print("\nAcertos: " )
        for i in self.letras_corretas:
            print(i + " ", end="")
        tentativa = input("\nFaça uma tentativa: ")
        self.VerificaTentativa(tentativa=tentativa)

    def VerificaTentativa(self, tentativa):
        for _ in self.palavra:
            if tentativa in self.letras_erradas or tentativa in self.letras_corretas:
                return
            elif tentativa in self.palavra:
                self.letras_corretas.append(tentativa)
                self.ModificaPalavraEscondida(tentativa=tentativa)
            else:
                self.letras_erradas.append(tentativa)

    def ModificaPalavraEscondida(self, tentativa):
        cont = 0
        for letra in self.palavra:
            if letra == tentativa:
                self.palavra_escondida[cont] = tentativa
            cont += 1

    def Continuajogo(self):
        if len(self.letras_erradas) < 6 and '_' in self.palavra_escondida:
            return True
        else:
            return False


class Main():

    def __init__(self):
        self.game = Forca()
        while self.game.Continuajogo():
            self.game.ImprimeJogo()
            os.system("cls")

        if "_" in self.game.palavra_escondida:
            print("Você perdeu!!")
        else:
            print("Você venceu!!")



main = Main()
