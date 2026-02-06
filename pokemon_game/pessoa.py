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
    def __init__(self, nome=None, pokebola=None, dinheiro=100):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        if pokebola is None: 
            self.pokebola = []
        else: 
            self.pokebola = pokebola


        self.dinheiro = dinheiro


    def __str__(self):
        return self.nome
    

    def mostrar_pokebola(self):

        if self.pokebola:
            print("\n", "-"*50, f"\n\nPokebola de [ {self} ]: ")

            for index, pokemon in enumerate(self.pokebola):
                print(f"{index+1} - {pokemon}")
            print("\n", "-"*50)
        else:
            print("\n","-"*50,f"\n\n{self} não tem nenhum Pokemon","\n", "-"*50)


    def escolher_pokemon(self):
        if self.pokebola:
            pokemon_escolhido = random.choice(self.pokebola)
            print(f">> {self} escolheu {pokemon_escolhido}")

            return pokemon_escolhido
        
        else:
            print("\nERRO: Esse jogador não possui nenhum pokemon para ser escolhido!") 

    
    def mostrar_dinheiro(self):
        print(f"\nVocê possui ${self.dinheiro} em sua conta")  


    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f"Você ganhou ${quantidade}") 
        self.mostrar_dinheiro()
             
    def batalhar(self, pessoa):
        print(f"\n{self} iniciou uma batalha contra {pessoa}")

        pessoa.mostrar_pokebola()
        pokemon_inimigo = pessoa.escolher_pokemon()
        meu_pokemon = self.escolher_pokemon()

        if meu_pokemon and pokemon_inimigo:
            while True: 
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                
                if vitoria:
                    print(f"\n{self} venceu a batalha")
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)

                if vitoria_inimiga:
                    print(f"\n{pessoa} venceu a batalha")
                    break
                              
        else: 
            print("Está batalha não pode ocorrer...") 

        
class Player(Pessoa):
    tipo = "player"


    def capturar(self, pokemon):
        self.pokebola.append(pokemon)
        print(f"\n>> {self} capturou {pokemon}")


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

    
    def explorar(self): 
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f"\n>> Um pokemon selvagem apareceu: {pokemon}")

            capturar = input("\nDeseja capturar o Pokemon? (s/n): ") 
            if capturar == "s":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f"\n>> O pokemon {pokemon} fugiu")
            else:
                print("\n>> Ok, boa viagem")

        else:
            print("\n >> Essa exploração não deu em nada") 


class Inimigo(Pessoa):
    tipo = "inimigo"
    
    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []

            for _ in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokebola=pokemons_aleatorios)
        
        else:
            super().__init__(nome=nome, pokebola=pokemons)

