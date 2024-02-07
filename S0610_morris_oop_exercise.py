"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
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
        self.sleepiness = max(0, self.sleepiness)
        self.thirst = max(0, self.thirst)
        self.hunger = max(0, self.hunger)
        self.whisky = max(0, self.whisky)
        self.gold = max(0, self.gold)


morris = Miner()


for turn in range(1, 1001):
    morris.do_something()


    print(f"Turn {turn}: Sleepiness: {morris.sleepiness}, Thirst: {morris.thirst}, Hunger: {morris.hunger}, Whisky: {morris.whisky}, Gold: {morris.gold}")


print(f"\nMorris' Total Gold after 1000 turns: {morris.gold}")
