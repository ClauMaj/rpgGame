
import random
# Main character class
class Character:
    def __init__(self, name, health, power,armor,evade, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty
        self.armor = armor
        self.evade = evade
    def attack(self, target):
        # considers armor and if solves case when target.armor > self.power wich would add HP if not
        heroAttack = self.power - target.armor
        if heroAttack > 0:
            target.health -= heroAttack
            print(f"\n{self.name} does {heroAttack}  ⚔ damage to {target.name}!")
        else:
            print(f"{target.name}'s armor blocked all damage.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            print(f"\n{self.name} is dead. ☠")
            return False
    def status(self):
        if self.health > 0:
            return f"{self.name} => {self.health} ♡ health | {self.power} 🗡 power | {self.armor} ⛨ armor | {self.evade} ✴ evade chance | {self.bounty} ₿ coins."
        else:
            return f"{self.name} is dead. ☠"
    def takeCoins(self,target):
        if target.health <=0 and type(target) != Zombie:
            self.bounty += target.bounty
            print(f"{self.name} defeated {target.name} and looted {target.bounty} coins.")
            target.bounty = 0
    def buy(self, item):
        self.bounty -= item.cost

#Class hero 20% chance of Double Damage
class Hero(Character):
    def __init__(self, name, health, power,armor,evade, bounty):
        super(Hero,self).__init__(name, health, power,armor,evade, bounty)
        # considers armor and if solves case when target.armor > self.power wich would add HP if not
        #roll for hero 20% chance of Double Damage
    def attack(self, target):
        roll = random.randint(1,10)
        heroAttack = self.power - target.armor
        if roll in range (1,9):
            if heroAttack > 0:
                target.health -= heroAttack
                print(f"\n{self.name} does {heroAttack} ⚔ damage to {target.name}!")
            else:
                print(f"{target.name}'s armor blocked all damage.")
        else:
            if heroAttack > 0:
                target.health -= heroAttack*2
                print(f"\n{self.name} does {heroAttack*2} ⚔ Double Damage to {target.name}!")
            else:
                print(f"{target.name}'s armor blocked all damage.")
# Basic villan
class Goblin(Character):
    def __init__(self, name, health, power,armor,evade, bounty):
        super(Goblin,self).__init__(name, health, power,armor,evade, bounty)
# Immortal villan
class Zombie(Character):
    def __init__(self,name, health, power,armor,evade, bounty):
        super(Zombie,self).__init__(name, health, power,armor,evade, bounty)
    def alive(self):
        return True
    def status(self):
            return f"{self.name} is immortal."

# medic class 20% chance to heal 2 HP every time is attacked
class Medic(Character):
    def __init__(self, name, health, power,armor,evade, bounty):
        super(Medic,self).__init__(name, health, power,armor,evade, bounty)
    def heal(self):
        roll = random.randint(1,10)
        if roll in range (1,3):
            self.health += 2
            print(f"\n{self.name} heals ✙  2 HP!")
# Shadow class low HP but 90% chance to dodge attack
class Shadow(Character):
    def __init__(self,name, health, power,armor,evade, bounty):
        super(Shadow,self).__init__(name, health, power,armor,evade, bounty)
    #roll a 10% chance of hit against shadow and if true takes basic character.attack
    def shadowAttack(self,enemy):
        roll = random.randint(1,10)
        if roll in range (5,6):
            enemy.attack(self)
        else:
            print("\nShadow dodged the attack.")
#Clumsy class insane damage but 90% chance to miss attack
class Clumsy(Character):
    def __init__(self,name, health, power,armor,evade, bounty):
        super(Clumsy,self).__init__(name, health, power,armor,evade, bounty)
#roll for 10% hit chance for clumsy and check damage-armor ratio    
    def attack(self, target):
        heroAttack = self.power - target.armor
        roll = random.randint(1,10)
        if roll in range (1,2):
            if heroAttack > 0:
                target.health -= heroAttack
                print(f"\n{self.name} does {heroAttack} ⚔ damage to {target.name}!")
            else:
                print(f"{target.name}'s armor blocked all damage.")
        else:
            print(f"\n{self.name}'s attack missed!")

# items in shop
class Tonic(object):
    cost = 5
    name = 'Tonic'
    def apply(self, character):
        character.health += 2
        print(f"{character.name}'s health increased to {character.health}.")
class Sword(object):
    cost = 10
    name = 'Sword'
    def apply(self, hero):
        hero.power += 2
        print(f"{hero.name}'s power increased to {hero.power}.")
class SuperTonic(object):
    cost = 10
    name = 'Super Tonic'
    def apply(self, hero):
        hero.health += 10
        print(f"{hero.name}'s health increased to {hero.health}.")

#shop menu
class Store(object):
    items = [Tonic, Sword, SuperTonic]
    def do_shopping(self, pickedHero):
        while True:
            print("\n=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"{pickedHero.status()}")
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f"{i+1}. buy {item.name} => {item.cost} coins.")
            print("9. leave")
            pick = int(input(">>>>>>>>>>>> "))
            if pick == 9:
                break
            else:
                ItemToBuy = Store.items[pick - 1]
                item = ItemToBuy()
                if pickedHero.bounty - item.cost >= 0:
                    pickedHero.buy(item)
                    item.apply(pickedHero)
                else:
                    print("\nSorry, you don't have enough coins.")
# created characters
# name, health, power,armor,evade, bounty
hero = Hero("Claude", 10, 5,0,0, 5) # 20% chance of Double Damage
goblin = Goblin("Python", 6, 2 ,0,0, 5) # just a goblin
zombie = Zombie("Zombie", 0 ,2,0,0,5) # Immortal
medic = Medic("Medic", 10, 5,0,0,5) # 20% chance to heal 2 HP every time is attacked
shadow = Shadow("Shadow", 1, 5,0,0,5) # low HP but 90% chance to dodge attack
clumsy = Clumsy("Clumsy", 5, 10,0,0,5) # insane damage but 90% chance to miss attack
wizard = Goblin("Wizard", 6,2,0,0,6) # just a goblin
boss = Goblin("Boss",6,2,0,0,5) # just a goblin

# 1st menu to pick a hero
def pick():
    print("\n++++++++++++ Welcome - Let the games BEGIN!++++++++++++++")
    print(f"""\t    ======================
    \t     ✯  Pick your HERO! ✯
\t    ======================
1. {hero.status()} =special atribute> has a 20% chance of Double Damage
2. {medic.status()} =special atribute> has a 20% chance to heal 2 HP every time is attacked
3. {shadow.status()} =special atribute> has very low HP but 90% chance to dodge attacks
4. {clumsy.status()} =special atribute> has insane damage but 90% chance to miss attacks""")
    pick = input(">>>>>>>>>>>>>>> ")
    if pick =="1":
        return hero
    elif pick == "2":
        return medic
    elif pick == "3":
        return shadow
    elif pick == "4":
        return clumsy
    

# second menu to pick an enemy
def menu():
    print("\n-----------------------------------------")
    print(f"{pickedHero.status()}")
    print("-------------Available targets-------------")
    print(f"{goblin.status()}")
    print(f"{wizard.status()}")
    print(f"{boss.status()}")
    print(f"{zombie.status()}")
    print("""\nWhat do you want to do?
=====================
1. fight goblin
2. fight wizard
3. fight boss
4. fight zombie
5. enter store
6. flee""")
    return input(">>>>>>>>>>>>>>> ")


# fight function
def fight(pickedHero,villan):
    if pickedHero.alive() and villan.alive():
        # roll 50 50 chance for hero or villan to atttack
        roll = random.randint(1,100)
        # hero attacks
        if roll <= 50:
            pickedHero.attack(villan)
            pickedHero.takeCoins(villan)
        else:
        # villan attacks
            #if shadow dodge chance
            if type(pickedHero) == Shadow:
                pickedHero.shadowAttack(villan)
                pickedHero.takeCoins(villan)
            else:    
                villan.attack(pickedHero)
            # if medic 20% chance to heal after attack
            if type(pickedHero) == Medic:
                pickedHero.heal()
            # after attack...check if hero still alive
            if not pickedHero.alive():
                print("\nGAME OVER!!! See you next time, warrior!!!")
                exit()
    else:
        # if not pickedHero.alive():
        #     print(f"\nYour Hero {pickedHero.name} is dead!")
        # elif not villan.alive():
        #     print(f"\nThe villan {villan.name} is already dead!")
        pass

#program starts
pickedHero = pick()        
choice = menu()

# loop for each enemy pick
while choice != "6":
    if choice =="1":
        fight(pickedHero,goblin)
        
        choice = menu()
    elif choice == "4":
        fight(pickedHero,zombie)
        choice = menu()
    elif choice == "2":
        fight(pickedHero,wizard)
        choice = menu()
    elif choice == "3":
        fight(pickedHero,boss)
        choice = menu()
    elif choice == "5":
        shopping_engine = Store()
        shopping_engine.do_shopping(pickedHero)
        choice = menu()
    else:
        print(f"Invalid input {choice}")
        choice = menu()

print("\nYOU WIN!!! See you next time, warrior!!!")

#finished adding armor => add the evade functionalyty