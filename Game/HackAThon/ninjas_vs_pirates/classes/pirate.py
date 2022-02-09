import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.spechit = 0

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"{ninja.name} took damage! They have {ninja.health} left!")
        self.pirateTalk()
        return self
    def Special(self, ninja):
        if ninja.spechit == 0:
            print(f"**{self.name} stabs his sword into the ground, rips off his hook, and reveals a hidden arm cannon!**")
            print(f"**{self.name} fires off three rounds from his arm cannon! -Boom Boom Boom- **")    
            ninja.health -= self.strength + 3
            ninja.spechit += 1
        elif ninja.spechit == 2:
            print(f"**{self.name} ran out of cannonballs!**")
            print("Arrrgh! Out'o ammo")
        return self
# created attrib spechit to limit specials to two

    def pirateTalk(self):
        speech = [
            f'{self.name} says: off the plank with you! *hick up*',
            f'{self.name} says: I know you have my booty!',
            f'{self.name} says: Ive lost my leg once, IT WONT HAPPEN AGAIN!',
            f'{self.name} says: I only have 1 arm, 1 leg and 1 eye, and ill still beat you!']
        print(random.choice(speech))
        return self

    def buff(self):
        print(f"{self.name}Unscrews hook hand and puts on corkscrew hand to uncork rum and drinks")
        self.health += 5



