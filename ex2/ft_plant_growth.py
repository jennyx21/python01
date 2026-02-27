class Plant:

    def __init__(self, name: str, hight: int, days: int):
        self.name = name
        self.hight = hight
        self.days = days

    def grow(self, days: int):
        self.hight += days

    def age(self, days):
        self.days += days

    def get_info(self):
        return f"{self.name}: {self.hight}cm, {self.days} days old"


def ft_plant_growth():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
        ]

    days: int = 7

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    print(f"=== Day {days} ===")
    for plant in plants:
        plant.age(days)
        plant.grow(days)
        print(plant.get_info())


if __name__ == "__main__":
    ft_plant_growth()
