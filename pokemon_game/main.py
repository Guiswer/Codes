#!/usr/bin/env python3

import pickle
from pokemon import *
from people import *


def choose_starter_pokemon(player):
    print(f"\n\t>> Hello {player}, you can now choose the Pokemon that will accompany you on this journey!") 

    pikachu = ElectricPokemon("Pikachu", level=1)
    charmander = FirePokemon("Charmander", level=1)
    squirtle = WaterPokemon("Squirtle", level=1)

    print("\n\tYou have 3 choices: \n")
    print("\n\t1 -", pikachu)
    print("\n\t2 -", charmander)
    print("\n\t3 -", squirtle)

    while True:
        choice = input("\nChoose your Pokemon: ")

        match choice:
            case "1":
                player.capture(pikachu)
                break

            case "2":
                player.capture(charmander)
                break

            case "3":
                player.capture(squirtle)
                break          
        
        print("\n⚠️\tInvalid choice!\n")

    print("\n", "-" * 30)
    

def save_game(player):
    try:
        with open("database.db", "wb") as file:
            pickle.dump(player, file)
    except Exception as error:
        print("\n\n\t⚠️  Error saving the game ⚠️")
        print(error)


def load_game():
    try:
        with open("database.db", "rb") as file:
            player = pickle.load(file)
            print("\nLoading successful") 
            return player
        
    except Exception:
        print("\n\n\t This is the first load/save to be made... cool! :D ")
        return None



if __name__ == "__main__": 

    print("\nWelcome to the Pokemon RPG Terminal Game!") 

    player = load_game()

    if not player:
        name = input("\nHello! Please type your name: ") 
        player = Player(name)

        print(f"""
            Hello {name}, this is a world inhabited by Pokemons. 
            From now on, your mission is to become a Pokemon Master!

            Capture as many Pokemons as possible to proceed and fight your enemies!  
        """)
        player.show_money()

        print("\n", "-"*100)
        
        if player.pokemons:
            print("\tI see you already have some Pokemons...") 
            player.show_pokemons()
        else:
            print("\n\tYou don't have any Pokemons, so you need to choose one...")
            choose_starter_pokemon(player)

        print("\n\tGreat! Now that you have a Pokemon, face your childhood rival, Gary!") 

        print("\n", "-"*50)
        
        gary = Enemy(name="Gary", pokemons=[WaterPokemon("Squirtle", level=1)])
        player.battle(gary)

        save_game(player)


    while True:
        print(f"""
            \nWhat would you like to do?

            1 - Explore the world
            2 - Fight an enemy
            3 - PokeDex (Show Pokemons)    
            0 - Exit game
              
        """)

        choice = input("\n\tYour choice: ")

        match choice:
            case "0":
                print("Goodbye!")
                break
            case "1": 
                player.explore()
                save_game(player)
            case "2":
                enemy_a = Enemy()
                player.battle(enemy_a)
                save_game(player)
            case "3":
                player.show_pokemons()
            case _:
                print("\n⚠️  Invalid choice...  ⚠️")

print()