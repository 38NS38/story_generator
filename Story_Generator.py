import random as rnd 

# Story-Parts

when = ("Gestern","Letze woche","Vor einem Jahr","Vorhin")
person = ("mit meinem Vater","mit meinem Bruder","mit meiner Mutter", "mit meinem Lehrer")
location = ("in ein Striptclub","zur kirmes","zur Polizei","ins Gefängniss")
animal = ("einem Löwen","einem Bär","einer Katze","einer Biene")
liquid = ("Blut","Wasser","Wein","Milch")
action = ("gekämpft","gespielt","gebumst")



# Choice of word in the Story-Parts

random_when = rnd.choice(when)
random_person = rnd.choice(person)
random_location = rnd.choice(location)
random_animal = rnd.choice(animal)
random_liquid = rnd.choice(liquid)
random_action = rnd.choice(action)


#Main-Story,filled with random Choices of Story-Parts

print(random_when + " bin ich " + random_person + " " + random_location + " gegangen." + """
Dort haben wir mit """ + random_animal + " " + random_action + " und danach haben wir" + """
zusammen eine Flasche """ + random_liquid +" getrunken." )

