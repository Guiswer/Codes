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

    def __str__(self):
        return f"{self.nome} (lvl: {self.level})" 

    def atacar(self, pokemon):
        print(f"O {self} atacou {pokemon}!!\n")


class PokemonEletrico(Pokemon):
    tipo = "elétrico"

    def atacar(self, pokemon):
        print(f"\n{self} deu um [raio do trovão] em {pokemon}!\n")


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f"\n{self} lançou uma [bola de fogo] na cabeça de {pokemon}!\n")


class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print(f"\n{self} lançou um [jato d'água] em {pokemon}!\n")
