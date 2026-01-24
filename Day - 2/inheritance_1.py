#cara pertama atribut
class animal:
    def __init__(self, NAME, SPECIES):
        self.name = NAME
        self.species = SPECIES

    def eat(self):
        print('I am eating')

cat = animal('Meong', 'Mammal')

class carnivore(animal):
    def __init__(self, NAME, SPECIES):
        super().__init__(NAME, SPECIES)

lion = carnivore('Simba', 'Mammal')

class diet_carnivore(carnivore):
    def __init__(self, NAME, SPECIES):
        super().__init__(NAME, SPECIES)
        self.diet = 'meat'

class omnivore(animal):
    def __init__(self, NAME, SPECIES):
        super().__init__(NAME, SPECIES)

pig = omnivore('babi', 'Mammal')

class diet_omnivore(omnivore):
    def __init__(self, NAME, SPECIES):
        super().__init__(NAME, SPECIES)
        self.diet = 'meat and plant'

class herbivore(animal):
    def __init__(self, NAME, SPECIES):
        super().__init__(NAME, SPECIES)

cow = herbivore('Moo', 'Mammal')

class diet_herbivore(herbivore):
    def __init__(self, NAME, SPECIES):
        super().__init__(NAME, SPECIES)
        self.diet = 'plant'

print("Which food type you want to output")
print("1. Carnivore")
print("2. Omnivore")
print("3. Herbivore")