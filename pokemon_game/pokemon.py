#!/usr/bin/env python3

import random

class Pokemon: #abstract
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie 

        if level: 
            self.level = level
        else: 
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie
        
        self.ataque = self.level * 5
        self.vida = self.level * 10
    

    def __str__(self):
        return f"{self.nome} (lvl: {self.level})" 


    def atacar(self, pokemon):
 
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo


        print(f"{pokemon} perdeu {ataque_efetivo} pontos de vida!")
        
        if pokemon.vida <= 0:
            print(f"{pokemon} foi derrotado!") 
            return True
        else: 
            return False
        

class PokemonEletrico(Pokemon):
    tipo = "elétrico"

    def atacar(self, pokemon):
        print(f"\n{self} deu um [raio do trovão] em {pokemon}!\n")
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f"\n{self} lançou uma [bola de fogo] na cabeça de {pokemon}!\n")
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print(f"\n{self} lançou um [jato d'água] em {pokemon}!\n")
        return super().atacar(pokemon)
    
    