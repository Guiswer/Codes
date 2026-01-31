#!/usr/bin/env python3

from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(f"\nHello {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nesse jornada!") 

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("\nVocê possui 3 escolhas: \n")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        escolha = input("\nEscolha o seu Pokemon: ")

        match escolha:
            case "1":
                player.capturar(pikachu)
                break

            case "2":
                player.capturar(charmander) 
                break

            case "3":
                player.capturar(squirtle) 
                break           
        
        print("\n⚠️\tEscolha inválida!\n")

    print("\n", "-" * 30)
    

player = Player("Guiswer")
player.capturar(PokemonFogo("Charmander", level=1))

inimigo1 = Inimigo(nome="Gary", pokebola=[PokemonAgua("Squirtle", level=1)])


player.batalhar(inimigo1)














print()