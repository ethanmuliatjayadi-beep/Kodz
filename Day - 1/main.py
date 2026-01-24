import random
import time

class character:
    def __init__(self):
        self.name = ''
        self.classes = ''
        self.hp = 0
        self.mp = 0
        self.dmg = 0
        self.skill = ''
    def attacking(self, enemy):
        enemy.hp = enemy.hp - self.dmg

    def skills(self, skill):
        if self.skill == 'rage':
            self.hp += 15
        elif self.skill == 'wush':
            self.dmg += 5
        elif self.skill ==  'hammer pound':
            self.dmg += 8
            self.hp -= 5
        elif self.skill == 'gading serpong':
            self.hp += 30

#ODIN
odin = character()
odin.name = 'odin the first'
odin.classes = 'barbarians'
odin.hp = 100
odin.mp = 10
odin.dmg = odin.hp*0.1
odin.skill = 'rage'

#DODO
dodo = character()
dodo.name = 'dodo the nerd'
dodo.classes = 'nerd'
dodo.hp = 75
dodo.mp = 35
dodo.dmg = dodo.hp*0.2
dodo.skill = 'wush'

#JACEK
jacek = character()
jacek.name = 'jacek the viking'
jacek.classes = 'viking'
jacek.hp = 60
jacek.mp = 50
jacek.dmg = jacek.hp*0.1
jacek.skill = 'hammer pound'

#KEVIN
kevin = character()
kevin.name = 'kevin the ok'
kevin.classes = 'nerd'
kevin.hp = 50
kevin.mp = 60
kevin.dmg = kevin.hp*0.2
kevin.skill = 'wush'

#GADING SERPONG
tanggerang = character()
tanggerang.name = 'tanggerang bukan jakarta'
tanggerang.classes = 'kota'
tanggerang.hp = 110
tanggerang.mp = 10
tanggerang.dmg = dodo.hp*0.4
tanggerang.skill = 'gading serpong'

def select_player(player):
    if player == '1':
        return odin
    elif player=='2':
        return dodo
    elif player=='3':
        return jacek
    elif player=='4':
        return kevin
    elif player=='5':
        return tanggerang

print("1 : Odin || 2 : Dodo || 3 : Jacek || 4 : Kevin || 5 : Tanggerang")
player1 = input("Select player 1: ")
player2 = input("Select player 2:")
p1 = select_player(player1)
p2 = select_player(player2)

while True:
    if p1 == p2:
        print("You can't play with yourself")
        break
    p1.attacking(p2)
    if random.randint(1, 10) < 4:
        p1.skills(p1.skill)
        print(f'{p1.name} is using {p1.skill}')
    print(f'{p1.name} is attacking! {p2.name} hp is {p2.hp}')
    p2.attacking(p1)
    if random.randint(1, 10) < 4:
        p2.skills(p2.skill)
        print(f'{p2.name} is using {p2.skill}')
    print(f'{p2.name} is attacking! {p1.name} hp is {p1.hp}')
    
    if p2.hp <= 0:
        print(f'{p1.name} win')
        break
    elif p1.hp <= 0:
        print(f'{p2.name} win')
        break