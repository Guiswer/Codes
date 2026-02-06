#!/usr/bin/env python3

import pickle
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(f"\n\t>> Hello {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nesse jornada!") 

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("\n\tVocê possui 3 escolhas: \n")
    print("\n\t1 -", pikachu)
    print("\n\t2 -", charmander)
    print("\n\t3 -", squirtle)

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
    

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
    except Exception as error:
        print("\n\n\t⚠️  Erro ao salvar o jogo ⚠️")
        print(error)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("\nLoading feito com sucesso") 
            return player
        
    except Exception as error:
        print("\n\n\t Este é o primeiro load/save a ser feito... legal :D ")



if __name__ == "__main__": 

    print("\nBem-vindo ao game Pokemon RPG de terminal!") 

    player = carregar_jogo()

    if not player:
        nome = input("\nOlá, digite o seu nome: ") 
        player = Player(nome)

        print(f"""
            Olá {nome}, esse é um mundo habitado por pokemons,  a partir de agora sua missão é se tornar um mestre dos pokemons

            Capture o máximo de pokemons para prosseguir e lute com seus inimigos!  
        """)
        player.mostrar_dinheiro()

        print("\n", "-"*100)
        if player.pokebola:
            print("\tJá vi que você tem alguns pokemons...") 
            player.mostrar_pokemons()
        else:
            print("\n\tVocê não tem nenhum pokemon, portanto precisa escolher um...")
            escolher_pokemon_inicial(player)

        print("\n\tPronto, agora que você já possui um pokemon, enfrente seu arqui-rival desde o jardim de infância Gary") 

        print("\n", "-"*50)
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)

        salvar_jogo(player)


    while True:
        print(f"""
            \nO que deseja fazer?

            1 - Explorar o mundo
            2 - Lutar com um inimigo
            3 - PokeAgenda    
            0 - Sair do game
              
        """)

        escolha = input("\n\tSua escolha: ")

        match escolha:
            case "0":
                break
            case "1": 
                player.explorar()
                salvar_jogo(player)
            case "2":
                inimigoA = Inimigo()
                player.batalhar(inimigoA)
                salvar_jogo(player)
            case "3":
                player.mostrar_pokebola()
            case _:
                print("\n⚠️  Escolha inválida...  ⚠️")







print()