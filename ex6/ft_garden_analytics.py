class Plant:

    class Stats:
        def __init__(self) -> None:
            self.showen = 0
            self.aged = 0
            self.growen = 0

        def disply_stats(self) -> None:
            print(f"Stats: {self.growen} grow, {self.aged} "
                  f"age, {self.showen} show")

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.stats = Plant.Stats()

    def show(self) -> None:
        self.stats.showen += 1
        print(f"{self.name}: {round(self.height)}cm, "
              f"{self.days} days old")

    @staticmethod
    def is_older_than_year(days) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown Plant", 0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.blooming = False

    def show(self) -> None:
        super().show()
        print(f"collor: {self.color}")
        if self.blooming is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet.")

    def bloom(self) -> None:
        self.blooming = True

    def grow(self, days) -> None:
        self.stats.growen += 1
        self.height += 0.8 * days

    def age(self, days) -> None:
        self.stats.aged += 1
        self.days += days


class Seed(Flower):
    def __init__(self, name: str, height: int, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 days: int, trunk_diameter: int) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self.shade = 0

    def produce_shade(self) -> None:
        self.shade += 1
        print(f"Tree {self.name} now prduces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter} cm")

    def grow(self, days) -> None:
        self.stats.growen += 1
        self.height += 0.8 * days

    def age(self, days) -> None:
        self.stats.aged += 1
        self.days += days

    def shade_stats(self) -> None:
        print(f"{self.shade} shade")


class Vegteble(Plant):
    def __init__(self, name: str, height: int,
                 days: int, harvest_season: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrirional value: {self.nutritional_value}")

    def grow(self, days) -> None:
        self.stats.growen += 1
        self.height += 0.8 * days

    def age(self, days) -> None:
        self.stats.aged += 1
        self.days += days
        self.nutritional_value += days


def ft_plant_analytics() -> None:
    pine = Tree("Pine", 300, 400, 20)
    dandelion = Flower("Dandelion", 20, 200, "yellow")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    anonym = Plant.anonymous_plant()
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

    print("=== Check year-old")
    print(f"is {pine.days} days more than a year? -> "
          f"{pine.is_older_than_year(pine.days)}")
    print(f"is {dandelion.days} days more than a year? -> "
          f"{dandelion.is_older_than_year(dandelion.days)}")
    print()
    for flower in flowers:
        print("=== Flower")
        flower.show()
        print(f"[asking the {flower.name} to bloom]")
        flower.bloom()
        flower.show()
        flower.stats.disply_stats()
        print()

    for tree in trees:
        print("=== Tree")
        tree.show()
        tree.stats.disply_stats()
        tree.shade_stats()
        print(f"[asking the {tree.name} to produce shade]")
        tree.produce_shade()
        tree.stats.disply_stats()
        tree.shade_stats()
        print()

    for vegteble in vegtables:
        print("=== Vegatables")
        vegteble.show()
        print(f"[make {vegteble.name} grow and age for 20 days]")
        vegteble.grow(20)
        vegteble.age(20)
        vegteble.show()
        print()

    print("=== Seed")
    sunflower.show()
    print(f"seeds: {sunflower.seeds}")
    print(f"[Make {sunflower.name} grow, age and bloom]")
    sunflower.age(20)
    sunflower.grow(20)
    sunflower.bloom()
    sunflower.show()
    print(f"seeds: {sunflower.seeds}")
    print(f"[statistics for {sunflower.name}]")
    sunflower.stats.disply_stats()
    print()

    print("=== Anonymous")
    anonym.show()
    print(f"[statistics for {anonym.name}]")
    anonym.stats.disply_stats()


if __name__ == "__main__":
    ft_plant_analytics()
