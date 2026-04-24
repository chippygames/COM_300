
class Character:
    def __init__(self, name, health, attack,defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def info(self):
        return f"Character:{self.name}|Health:{self.health}/100|Attack:{self.attack}|Defence{self.defence}"


    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0
            print ("you dead")



    def heal(self,amount):
        self.health += amount
        if self.health >= 100:
            self.health = 100
            print ("way too much health")


    def attack_target(self,other_character):
        # if self.Legit_damage >= 0: self.Legit_damage = 0
        # Character = self.target
        # self.Legit_damage = damage_
        #     print f"{self.name} attacks {self.name}"

        damage = self.attack - other_character.defence

        if damage <= 0:
            damage = 0

        other_character.take_damage(damage)
        return f"{self.name} attacks {other_character} for {damage} damage!"


