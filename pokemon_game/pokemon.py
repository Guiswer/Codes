#!/usr/bin/env python3

import random

class Pokemon: # abstract
    def __init__(self, species, level=None, name=None):
        self.species = species

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if name:
            self.name = name
        else:
            self.name = species
        
        # Traduzi 'ataque' (atributo) para 'attack_power' para não confundir com o método 'attack'
        self.attack_power = self.level * 5 
        self.health = self.level * 10
    

    def __str__(self):
        return f"{self.name} (lvl: {self.level})" 


    def attack(self, target): # Mudei o argumento 'pokemon' para 'target' para ficar mais claro
 
        effective_attack = int(self.attack_power * random.random() * 1.3)
        target.health -= effective_attack

        print(f"{target} lost {effective_attack} health points!")
        
        if target.health <= 0:
            print(f"{target} was defeated!") 
            return True
        else: 
            return False
        

class ElectricPokemon(Pokemon):
    type = "electric"

    def attack(self, target):
        print(f"\n{self} used [Thunderbolt] on {target}!\n")
        return super().attack(target)


class FirePokemon(Pokemon):
    type = "fire"

    def attack(self, target):
        print(f"\n{self} threw a [Fireball] at {target}'s head!\n")
        return super().attack(target)


class WaterPokemon(Pokemon):
    type = "water"

    def attack(self, target):
        print(f"\n{self} cast a [Water Jet] at {target}!\n")
        return super().attack(target)