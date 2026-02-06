#!/usr/bin/env python3

import random
from pokemon import *


NAMES = [
        "John", "Isabel", "Lorena", "Francisco", "Richard", "Diego", "Patricia", "Marcelo", "Gustavo", "Geronimo"
    ]

POKEMONS = [
    FirePokemon("Charmander"), 
    FirePokemon("Flareon"),
    FirePokemon("Charmeleon"),
    ElectricPokemon("Pikachu"), 
    ElectricPokemon("Raichu"),
    WaterPokemon("Squirtle"),
    WaterPokemon("Magikarp") 
]


class Person:
    def __init__(self, name=None, pokemons=None, money=100):

        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        if pokemons is None: 
            self.pokemons = []
        else: 
            self.pokemons = pokemons


        self.money = money


    def __str__(self):
        return self.name
    

    def show_pokemons(self):

        if self.pokemons:
            print("\n", "-"*50, f"\n\nPokemons of [ {self} ]: ")

            for index, pokemon in enumerate(self.pokemons):
                print(f"{index+1} - {pokemon}")
            print("\n", "-"*50)
        else:
            print("\n","-"*50,f"\n\n{self} has no Pokemon","\n", "-"*50)
        
        self.show_money()


    def choose_pokemon(self):
        if self.pokemons:
            chosen_pokemon = random.choice(self.pokemons)
            print(f">> {self} chose {chosen_pokemon}")

            return chosen_pokemon
        
        else:
            print("\nERROR: This player has no pokemon to choose from!") 

    
    def show_money(self):
        print(f"\nYou have ${self.money} in your account")  


    def earn_money(self, amount):
        self.money += amount
        print(f"You earned ${amount}") 
        self.show_money()
             
    def battle(self, person):
        print(f"\n{self} started a battle against {person}")

        person.show_pokemons()
        enemy_pokemon = person.choose_pokemon()
        my_pokemon = self.choose_pokemon()

        if my_pokemon and enemy_pokemon:
            while True: 
                victory = my_pokemon.attack(enemy_pokemon)
                
                if victory:
                    print(f"\n{self} won the battle")
                    self.earn_money(enemy_pokemon.level * 100)
                    break

                enemy_victory = enemy_pokemon.attack(my_pokemon)

                if enemy_victory:
                    print(f"\n{person} won the battle")
                    break
                              
        else: 
            print("This battle cannot happen...") 

        
class Player(Person):
    type = "player"


    def capture(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"\n>> {self} captured {pokemon}")


    def choose_pokemon(self):
        self.show_pokemons()

        if self.pokemons:
            while True:
                try:
                    choice = int(input("Choose your Pokemon: "))
                    chosen_pokemon = self.pokemons[choice-1]
                    
                    print(f"\n>> {chosen_pokemon} I choose you !!\n") 

                    return chosen_pokemon

                except:
                    print("\n⚠️ Invalid choice!\n") 

        else:
            print("\nEmpty list...")

    
    def explore(self): 
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f"\n>> A wild pokemon appeared: {pokemon}")

            choice = input("\nDo you want to capture the Pokemon? (y/n): ")
            if choice == "y":
                if random.random() >= 0.5:
                    self.capture(pokemon)
                else:
                    print(f"\n>> The pokemon {pokemon} ran away")
            else:
                print("\n>> Ok, have a nice trip")

        else:
            print("\n >> This exploration yielded nothing") 


class Enemy(Person):
    type = "enemy"
    
    def __init__(self, name=None, pokemons=None):
        if not pokemons:
            random_pokemons = []

            for _ in range(random.randint(1, 6)):
                random_pokemons.append(random.choice(POKEMONS))

            super().__init__(name=name, pokemons=random_pokemons)
        
        else:
            super().__init__(name=name, pokemons=pokemons)