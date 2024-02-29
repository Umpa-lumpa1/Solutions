"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en klassemetode ved navn wag_tail for Dog.
    Denne metode udskriver i konsollen noget i stil med
    "Hunden Snoopy vifter med sin 32 cm lange hale"
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google det først.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Animal:
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"Animal(name='{self.name}', sound='{self.sound}', height={self.height}, weight={self.weight}, legs={self.legs}, female={self.female})"

    def make_noise(self):
        print("Roar")

class Dog(Animal):
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool, tail_length: int, hunts_sheep: bool):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return f"Animal(name='{self.name}', sound='{self.sound}', height={self.height}, weight={self.weight}, legs={self.legs}, female={self.female}, tail_length={self.tail_length}, hunts_sheep={self.hunts_sheep})"

    def wag_tail(self):
        print(f"hunden {self.name} vifter med sin {self.tail_length}cm lange hale")

    def make_noise(self):
        print(f"{self.sound}")

def mate(mother, father):
    #check gender.
    #find att for the puppy
    #make the puppy
    #return the puppy


animal1 = Animal(name="Lion", sound="Roar", height=1.2, weight=150, legs=4, female=False)
hund1 = Dog("buba", "bark", 0.6, 60, 4, False, 20, False)
hund2 = Dog("buba", "bark", 0.6, 60, 4, True, 20, False)

hund1.make_noise()
animal1.make_noise()
hund1.wag_tail()
mate(mother=hund2, father=hund1)
print(animal1)
print(hund1)
