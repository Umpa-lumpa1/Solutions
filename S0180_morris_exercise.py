"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""


"""def sleep():
    morris["sleepiness"] -= 10  # update sleepiness
    morris["thirst"] += 1  # update thirst
    morris["hunger"] += 1  # update hunger
    if morris["sleepiness"] < 0:  # check for values out of boundaries
        morris["sleepiness"] = 0

def mine():
    morris["sleepiness"] += 5  # update sleepiness
    morris["thirst"] += 5  # update thirst
    morris["hunger"] += 5  # update hunger
    morris["gold"] += 5

def drink():
    morris["sleepiness"] += 5  # update sleepiness
    morris["thirst"] -= 15  # update thirst
    morris["hunger"] -= 1  # update hunger
    morris["whisky"] -= 1

def eat():
    morris["sleepiness"] += 5  # update sleepiness
    morris["thirst"] -= 5  # update thirst
    morris["hunger"] -= 20  # update hunger
    morris["gold"] -= 2

def buy_whiskey():
    morris["sleepiness"] += 5  # update sleepiness
    morris["thirst"] += 1  # update thirst
    morris["hunger"] += 1  # update hunger
    morris["gold"] -= 1
    if morris["whisky"] < 10:
        morris["whisky"] = 10
def do_something():
    if morris["whisky"] == 0:
        buy_whiskey()
    elif morris["thirst"] > 95:
        drink()
    elif morris["hunger"] > 95:
        eat()
    elif morris["sleepiness"] > 84:
        sleep()
    else:
        mine()
def dead():
    return morris["sleepiness"] > 100 or morris["thirst"] > 100 or morris["hunger"] > 100


morris = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

while not dead() and morris["turn"] < 1000:
    morris["turn"] += 1
    do_something()
    print(morris)

class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1
        self.gold += 0

# Create Morris and initialize his attributes
morris = Miner()

# Simulate 1000 turns
for _ in range(1000):
    morris.sleep()
    morris.mine()
    morris.eat()
    morris.buy_whisky()
    morris.drink()

# Print Morris's total gold after 1000 turns
print(f"Morris' Total Gold after 1000 turns: {morris.gold}")


class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1
        self.gold += 0

# Create Morris and initialize his attributes
morris = Miner()

# Simulate 1000 turns
for turn in range(1, 1001):
    morris.sleep()
    morris.mine()
    morris.eat()
    morris.buy_whisky()
    morris.drink()

    # Print Morris's attributes after each turn
    print(f"Turn {turn}: Sleepiness: {morris.sleepiness}, Thirst: {morris.thirst}, Hunger: {morris.hunger}, Whisky: {morris.whisky}, Gold: {morris.gold}")

# Print Morris's total gold after 1000 turns
print(f"\nMorris' Total Gold after 1000 turns: {morris.gold}")"""

class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        self._check_attributes()

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5
        self._check_attributes()

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2
        self._check_attributes()

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1
        self._check_attributes()

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1
        self.gold += 0
        self._check_attributes()

    def do_something(self):
        if self.whisky == 0:
            self.buy_whisky()
        elif self.thirst > 95:
            self.drink()
        elif self.hunger > 95:
            self.eat()
        elif self.sleepiness > 84:
            self.sleep()
        else:
            self.mine()

    def _check_attributes(self):
        # Ensure attributes don't go below 0
        self.sleepiness = max(0, self.sleepiness)
        self.thirst = max(0, self.thirst)
        self.hunger = max(0, self.hunger)
        self.whisky = max(0, self.whisky)
        self.gold = max(0, self.gold)

# Create Morris and initialize his attributes
morris = Miner()

# Simulate 1000 turns
for turn in range(1, 1001):
    morris.do_something()

    # Print Morris's attributes after each turn
    print(f"Turn {turn}: Sleepiness: {morris.sleepiness}, Thirst: {morris.thirst}, Hunger: {morris.hunger}, Whisky: {morris.whisky}, Gold: {morris.gold}")

# Print Morris's total gold after 1000 turns
print(f"\nMorris' Total Gold after 1000 turns: {morris.gold}")

