#!/usr/bin/env python3

import random
from pokemon import *

NOMES = [
        "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego", "Patrícia", "Marcelo", "Gustavo", "Gerônimo"
    ]

POKEMONS = [
    PokemonFogo("Charmander"), 
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"), 
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp") 
]


class Pessoa:
    def __init__(self, nome=None, pokebola=None):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        if pokebola is None: 
            self.pokebola = []
        else: 
            self.pokebola = pokebola


    def __str__(self):
        return self.nome
    

    def mostrar_pokebola(self):

        if self.pokebola:
            print(f"\nPokebola de [ {self} ]: ")

            for index, pokemon in enumerate(self.pokebola):
                print(f"{index+1} - {pokemon}")
            print()
        else:
            print(f"\n{self} não tem nenhum Pokemon")


    def escolher_pokemon(self):
        self.mostrar_pokebola()

        if self.pokebola:
            while True:
                try:
                    escolha = int(input("Escolha o seu Pokemon: "))
                    pokemon_escolhido = self.pokebola[escolha-1]
                    
                    print(f"\n>> {pokemon_escolhido} eu escolho você !!\n") 

                    return pokemon_escolhido

                except:
                    print("\n⚠️ Escolha inválida!\n") 

        else:
            print("\nPokebola vazia...") 
            
             

    def batalhar(self, pessoa):
        print(f"\n{self} iniciou uma batalha contra {pessoa}")
        pessoa.mostrar_pokebola()

        self.escolher_pokemon()
        pessoa.escolher_pokemon()


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokebola.append(pokemon)
        print(f"\n{self} capturou {pokemon}")


class Inimigo(Pessoa):
    tipo = "inimigo"
    
    def __init__(self, nome=None, pokebola=None):
        super().__init__(nome=nome, pokebola=pokebola)
        
        if not pokebola:
            for _ in range(random.randint(1, 6)):
                pokebola.append(random.choice(POKEMONS))

    
    def escolher_pokemon(self):
        if self.pokebola:
            pokemon_escolhido = random.choice(self.pokebola)
            print(f">> {self} escolheu {pokemon_escolhido}")

            return pokemon_escolhido
        
        else:
            print("\nERRO: Esse jogador não possui nenhum pokemon para ser escolhido!") 
