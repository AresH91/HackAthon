import random
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.spechit = 0
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        print(f"{pirate.name} took damage! They have {pirate.health} left!")
        # def attack(self, pirate):
        pirate.health -= (self.strength + (self.speed*0.75))
        # pirate.health -= self.strength
        self.dialogue()
        return self

    def special(self, pirate):
        if pirate.spechit == 0:
            pirate.health -= (self.strength -(self.speed*0.25))
            print("{self.name} ducks and throws shuriken at the {pirate.name}")
            pirate.health -= self.strength + 3
            pirate.spechit += 1
        elif pirate.spechit == 2:
            print("Attack Failed")
        return self

    def special_buff(self):
        print(f'{self.name} sits down has a ramen')
        self.health += 5
        return self

    def dialogue(self):
        speech=[
                f'{self.name} says: show me your moves',
                f'{self.name} says: this is going to be easy']
        print(random.choice(speech))
        return self
