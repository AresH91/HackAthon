from cgitb import reset
from xml.etree.ElementTree import TreeBuilder
from classes.ninja import Ninja
from classes.pirate import Pirate
import random
import time

print("~Totally Rad Game Music Plays~")
print("Welcome Player to Ninjas vs Pirates")
print("You will be the Ninja, Naruto! Your goal is to defeat the Evil Pirate Lord!")

naruto = Ninja("Naruto")

jack = Pirate("Jack Sparrow")

play = True

while play:
    ninjaabil = [naruto.attack(jack), naruto.special(jack), naruto.special_buff()]
    pirateabil = [jack.attack(naruto), jack.Special(naruto), jack.buff()]



    random.choice(ninjaabil)
    random.choice(pirateabil)
    time.sleep(1.5)
    if naruto.health <= 0 or jack.health <= 0:
        play = False





# michelangelo = Ninja("Michelanglo")


# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

# jack_sparrow.Special(michelangelo)
# jack_sparrow.Special(michelangelo)

