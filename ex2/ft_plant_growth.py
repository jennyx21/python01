class Plant:

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self, days) -> None:
        self.height += 0.8 * days

    def age(self, days) -> None:
        self.days += days

    def get_info(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.days} days old"


def ft_plant_growth() -> None:

    plant = Plant("Rose", 25, 30)
    days: int = 7
    start: int = plant.height

    for i in range(days):
        print(f"=== Day {i + 1} ===")
        plant.age(1)
        plant.grow(1)
        print(plant.get_info())
    end: int = plant.height
    print(f"Growth this week: {round(end - start)}cm")


if __name__ == "__main__":
    ft_plant_growth()
