class Plant:

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self, days) -> None:
        self.height += 0.8 * days

    def age(self, days) -> None:
        self.days += days

    def show(self) -> None:
        print(f"Created: {self.name}: {round(self.height, 1)}cm, "
              f"{self.days} days old")


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Oak", 200, 365),
        Plant("Fern", 15, 120)
        ]

    i: int = 0
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()
        i += 1
    print(f"Total Plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
