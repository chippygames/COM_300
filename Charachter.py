class Character:
    def __init__(self, name, health, attack,defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self .Legit_damage = target_defence - attack

    def __init__(self,target):
        self.target = target



    def info(self):
        return f"Character:{self.name} {self.health} {self.attack} {self.defence}"


    def take_damage(self, damage):
        health = self.health - damage
        if self.health >= 0: self.health = 0
            if self.health == 0:
                return f"{self.name} is defeated"


    def heal(self,heal):
         self.health += heal
            if self.health <= 100: self.health = 100
                if self.health == 100:
                    print(f"{self.name} is fully healed")


    def tareget(self, damage):
        if self.Legit_damage >= 0: self.Legit_damage = 0
            
            print f"{self.name} attacks {self.name}"


