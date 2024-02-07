"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:
        class definition / klasse definition
        constructor / konstruktor
        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attribut
        encapsulation: protected method / indkapsling: beskyttet metode
"""


# Define a class named Building
class Building:
    # Constructor method that initializes instance variables area, floors, and _value
    def __init__(self, area, floors, value):
        self.area = area
        self.floors = floors
        self._value = value

    # Adjusting the value and printing a message
    def renovate(self):
        print("Installing an extra bathroom...")
        self._adjust_value(10)

    # Is used to adjust the value by the procent value
    def _adjust_value(self, percentage):
        self._value *= 1 + (percentage / 100)
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


# Define a subclass named Skyscraper that inherits from Building
class Skyscraper(Building):

    # Override the renovate method in the subclasskehrfje
    def renovate(self):
        print("Installing a faster elevator.")
        self._adjust_value(6)


# Create an instance of the Building class named small_house
small_house = Building(160, 2, 200000)

# Create an instance of the Skyscraper class named skyscraper
skyscraper = Skyscraper(5000, 25, 10000000)

# Looks through a list of buildings (small_house and skyscraper)
for building in [small_house, skyscraper]:
    # Print information about the building's floors and area
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.')
    # Call the renovate method for each building
    building.renovate()
