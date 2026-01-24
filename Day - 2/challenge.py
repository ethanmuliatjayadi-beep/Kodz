import random

class character:
    def __init__(self, NAME, HEALTH, DMG, MP):
        self.name = NAME
        self.health = HEALTH
        self.dmg = DMG
        self.mp = MP

    def attack(self, enemy):
        enemy.health -= self.dmg

    def skill_use(self):
        if self.skill == "Boost":
            self.health += 10
            self.dmg += 30
            self.mp += 50

        elif self.skill == "health Boost":
            self.health += 50
            self.mp += 5

        elif skill == "Damage Boost":
            self.dmg += 55
            self.mp -= 20

class hunter(character):
    def __init__(self, NAME, HEALTH, DMG, MP):
        super().__init__(NAME, HEALTH, DMG, MP)

        self.skill = "Boost"

class assasin(character):
    def __init__(self, NAME, HEALTH, DMG, MP):
        super().__init__(NAME, HEALTH, DMG, MP)

        self.skill = "health Boost"

class knight(character):
    def __init__(self, NAME, HEALTH, DMG, MP):
        super().__init__(NAME, HEALTH, DMG, MP)

        self.skill = "Damage Boost"

Ilham = hunter("Ilham", 200, 5, 10)
Hadi = hunter("Hadi", 180, 5, 10)

Joko = assasin("Joko", 120, 20, 10)
Kevin = assasin("Kevin", 105, 20, 10)

Andi = knight("Andi", 150, 5, 50)
Joni = knight("Joni", 145, 5, 50)

def pilih(player):
    if player == "1":
        return Ilham
    elif player == "2":
        return Hadi
    elif player == "3":
        return Joko
    elif player == "4":
        return Kevin
    elif player == "5":
        return Andi
    elif player == "6":
        return Joni

print("1. Ilham, 2. Hadi, 3. Joko, 4. Kevin, 5. Andi, 6. Joni")
player1 = input("Pilih player 1: ")
player2 = input("Pilih player 2: ")
p1 = pilih(player1)
p2 = pilih(player2)

while True:
    p1.attack(p2)
    p2.attack(p1)
    print(f"{p1.name} is attacking {p2.name}, {p1.name} has {p1.health} health")
    if random.randint(1, 10) < 9:
        p1.skill_use()
        print(f"{p1.name} is using {p1.skill}")
    print(f"{p2.name} is attacking {p1.name}, {p2.name} has {p2.health} health")
    if random.randint(1, 10) < 9:
        p2.skill_use()
        print(f"{p2.name} is using {p2.skill}")
    if p1.health <= 0:
        print(f"{p2.name} win")
        break
    elif p2.health <= 0:
        print(f"{p1.name} win")
        break