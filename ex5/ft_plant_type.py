class Plant:

    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str, ):
        super().__init__(name, height, days)
        self.color = color
        self.blooming = False

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.days} days old")
        print(f"collor: {self.color}")
        if self.blooming == True:
            print(f"{self.name} is blooming beautifully!")
        else: 
            print(f"{self.name} has not bloomed yet.")


    def bloom(self):
        self.blooming = True

    def grow(self, days):
        self.height += 0.8 * days


class Tree(Plant):
    def __init__(self, name: str, height: int, days: int, trunk_diameter: int):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self.name} now prduces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.days} days old")
        print(f"Trunk diameter: {self.trunk_diameter} cm")

    def grow(self, days):
        self.height += 0.8 * days


class Vegteble(Plant):
    def __init__(self, name: str, height: int, days: int, harvest_season: str):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        print(f"{self.name}: {round(self.height)}cm, "
              f"{self.days} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrirional value: {self.nutritional_value}")

    def grow(self, days):
        self.height += 0.8 * days
        
    def age(self, days):
        self.days += days
        self.nutritional_value += days


def ft_plant_type() -> None:
    flowers = [
        Flower("Rose", 25, 30, "red"),
        # Flower("Dandelion", 20, 200, "yellow")
        ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        # Tree("Pine", 200, 500, 20)
        ]

    vegtables = [
        Vegteble("Tomato", 80, 90, "summer"),
        # Vegteble("Cucumber", 40, 70, "summer")
        ]
    print("=== Garden Plant Types ===\n")
    for flower in flowers:
        print("=== Flower")
        flower.show()
        print(f"[asking the {flower.name} to bloom]")
        flower.bloom()
        flower.show()
        print()

    for tree in trees:
        print("=== Tree")
        tree.show()
        print(f"[asking the {tree.name} to produce shade]")
        tree.produce_shade()
        print()

    for vegteble in vegtables:
        print("=== Vegatables")
        vegteble.show()
        print(f"[make {vegteble.name} grow and age for 20 days]")
        vegteble.grow(20)
        vegteble.age(20)
        vegteble.show()
        print()


if __name__ == "__main__":
    ft_plant_type()
