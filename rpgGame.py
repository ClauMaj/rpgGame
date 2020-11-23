
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
    def evadeChance(self,target):
        #target.evade    0-2=10%, 3-4=20% 5-6=30% 7-8=40% 9+ = 50%
        # the evade is calculated here and applied before each attack
        if target.evade in range(0,3):
            if random.randint(1,11) in range(4,5):
                return True
        elif target.evade in range(3,5):
            if random.randint(1,11) in range(4,6):
                return True
        elif target.evade in range(5,7):
            if random.randint(1,11) in range(4,7):
                return True
        elif target.evade in range(7,9):
            if random.randint(1,11) in range(4,8):
                return True
        elif target.evade >= 9:
            if random.randint(1,11) in range(4,9):
                return True
        return False

    def attack(self, target):
        # considers armor and it solves case when target.armor > self.power wich would add HP if not
        if self.evadeChance(target) == True:
            print(f"{target.name} evaded the attack.")
            return
        heroAttack = self.power - target.armor
        if heroAttack > 0:
            target.health -= heroAttack
            print(f"\n{self.name} does {heroAttack}  ⚔ damage to {target.name}!")
        else:
            print(f"{target.name}'s armor blocked all damage.")
        # checks .health alive or dead
    def alive(self):
        if self.health > 0:
            return True
        else:
            print(f"\n{self.name} is dead. ☠")
            return False
            # print status
    def status(self):
        if self.health > 0:
            return f"{self.name} => {self.health} ♡ health | {self.power} 🗡 power | {self.armor} ⛨ armor | {self.evade} ✴ evade chance | {self.bounty} ₿ coins."
        else:
            return f"{self.name} is dead. ☠"
            # after each attack if villan dies the hero takes the coins
    def takeCoins(self,target):
        if target.health <=0 and type(target) != Zombie:
            self.bounty += target.bounty
            print(f"{self.name} defeated {target.name} and looted {target.bounty} coins.")
            target.bounty = 0
            #buy items from store
    def buy(self, item):
        self.bounty -= item.cost

#Class hero 20% chance of Double Damage
class Hero(Character):
    def __init__(self, name, health, power,armor,evade, bounty):
        super(Hero,self).__init__(name, health, power,armor,evade, bounty)
        # considers armor and if solves case when target.armor > self.power wich would add HP if not
    def attack(self, target):
        if self.evadeChance(target) == True:
            print(f"{target.name} evaded the attack.")
            return
        roll = random.randint(1,10)     #roll for hero 20% chance of Double Damage
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
        return f"{self.name} is immortal"

# medic class 20% chance to heal 2 HP every time is attacked
class Medic(Character):
    def __init__(self, name, health, power,armor,evade, bounty):
        super(Medic,self).__init__(name, health, power,armor,evade, bounty)
    def heal(self):
        # random 20% chance of heal
        roll = random.randint(1,10) 
        if roll in range (1,3):
            self.health += 2
            print(f"\n{self.name} heals ✙ 2 HP!")

# Shadow class low HP but 90% chance to dodge attack
class Shadow(Character):
    def __init__(self,name, health, power,armor,evade, bounty):
        super(Shadow,self).__init__(name, health, power,armor,evade, bounty)

#Clumsy class insane damage but 90% chance to miss attack
class Clumsy(Character):
    def __init__(self,name, health, power,armor,evade, bounty):
        super(Clumsy,self).__init__(name, health, power,armor,evade, bounty)
#roll for 10% hit chance for clumsy and check damage-armor ratio    
    def attack(self, target):
        if self.evadeChance(target) == True:
            print(f"{target.name} evaded the attack.")
            return
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
    def apply(self, shopper):
        shopper.health += 2
        print(f"\n{shopper.name}'s health increased to {shopper.health}.")
class Sword(object):
    cost = 10
    name = 'Sword'
    def apply(self, shopper):
        shopper.power += 2
        print(f"\n{shopper.name}'s power increased to {shopper.power}.")
class SuperTonic(object):
    cost = 10
    name = 'Super Tonic'
    def apply(self, shopper):
        shopper.health += 10
        print(f"\n{shopper.name}'s health increased to {shopper.health}.")
class Evade(object):
    cost = 7
    name = 'Evade'
    def apply(self, shopper):
        shopper.evade +=2
        print(f"\n{shopper.name}'s evade increased to {shopper.evade}.")

#shop menu
class Store(object):
    items = [Tonic, Sword, SuperTonic,Evade] #list of items
    # function to select an item and apply on the hero
    def do_shopping(self, pickedHero):
        while True: # repeat untill user exits
            print("\n=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"{pickedHero.status()}")
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f"{i+1}. buy {item.name} => {item.cost} coins.")
            print("9. leave shop and return to battle")
            pick = int(input(">>>>>>>>>>>> "))
            if pick == 9:
                break
            else:
                selected = Store.items[pick - 1]
                bought = selected()
                if pickedHero.bounty - bought.cost >= 0:
                    pickedHero.buy(bought)
                    bought.apply(pickedHero)
                else:
                    print("\nSorry, you don't have enough coins.")

# created characters
# name, health, power,armor,evade, bounty
hero = Hero("Claude", 10, 5,0,2, 100) # 20% chance of Double Damage
goblin = Goblin("Python", 6, 2 ,0,0, 5) # just a goblin
zombie = Zombie("Zombie", 0 ,2,0,0,5) # Immortal
medic = Medic("Medic", 10, 5,0,0,5) # 20% chance to recover 2 HP every time is attacked
shadow = Shadow("Shadow", 1, 5,0,2,5) # low HP but 90% chance to dodge attack
clumsy = Clumsy("Clumsy", 5, 10,0,2,5) # insane damage but 90% chance to miss attack
wizard = Goblin("Wizard", 6,2,0,2,6) # just a goblin
boss = Goblin("Boss",6,2,0,0,5) # just a goblin

# 1st menu to pick a hero
def pick():
    print("\n++++++++++++ Welcome - Let the games BEGIN!++++++++++++++")
    print(f"""\t    ======================
    \t     ✯  Pick your HERO! ✯
\t    ======================
1. {hero.status()} =special atribute> has a 20% chance of Double Damage
2. {medic.status()} =special atribute> has a 20% chance to recover 2 HP every time is attacked
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
    print(f"{zombie.status()} and has 2 🗡 power | 0 ⛨ armor | 0 ✴ evade chance |")
    print("""\nWhat do you want to do?
=====================
1. fight goblin
2. fight wizard
3. fight boss
4. fight zombie
5. enter store
6. Swap Power round
7. flee""")
    return input(">>>>>>>>>>>>>>> ")


# fight function
def fight(pickedHero,villan):
    if pickedHero.alive() and villan.alive():
        # roll 50 50 chance for hero or villan to attack
        roll = random.randint(1,100)
        # hero attacks
        if roll <= 50:
            pickedHero.attack(villan)
            pickedHero.takeCoins(villan)
        else:
        # villan attacks
            tempHealth = pickedHero.health # stores the hero health before is attacked(for medic)
            #if shadow dodge chance
            if type(pickedHero) == Shadow:
                #roll a 10% chance of hit against shadow 
                roll = random.randint(1,10)
                if roll in range (5,6):
                    villan.attack(pickedHero)
                else:
                    print("\nShadow dodged the attack.")
            else:    
                villan.attack(pickedHero)
            # if medic 20% chance to heal after attack
            if type(pickedHero) == Medic:
                if pickedHero.health < tempHealth:
                    pickedHero.heal()
            # after attack...check if hero still alive
            if not pickedHero.alive():
                print("\nGAME OVER!!! See you next time!!!")
                exit()
    else:
        # if not pickedHero.alive():
        #     print(f"\nYour Hero {pickedHero.name} is dead!")
        # elif not villan.alive():
        #     print(f"\nThe villan {villan.name} is already dead!")
        pass

def do_swap(swapHero):
    enemies = [goblin,wizard,boss,zombie]
    print("\n=====================")
    print(f"Welcome to the Swap Power round, {swapHero.name}! Who would you like to fight?")
    print("=====================")
    for i in range(len(enemies)):
        item = enemies[i]
        print(f"{i+1}. fight {item.name}!")
    print("9. return to main menu")
    swapPick = int(input(">>>>>>>>>>>> "))
    if swapPick == 9:
        return
    else:
        #risk swap power and double enemy bounty
        selected = enemies[swapPick-1]
        c = swapHero.power
        swapHero.power = selected.power
        selected.power = c
        d = selected.bounty
        selected.bounty +=d
        #swaped power fight
        fight(pickedHero,selected)
        #restore power and if villan not dead restore bounty
        selected.power = swapHero.power
        swapHero.power = c
        if selected.bounty > 0:
            selected.bounty -= d

#program starts
pickedHero = pick()        
choice = menu()

# loop for each pick
while choice != "7":
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
        shopStart = Store()
        shopStart.do_shopping(pickedHero)
        choice = menu()
    elif choice == "6":
        do_swap(pickedHero)
        choice = menu()
    else:
        print(f"Invalid input {choice}")
        choice = menu()



print("\nYOU WIN!!! See you next time!!!")

