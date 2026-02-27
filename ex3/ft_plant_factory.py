class Plant:

    def __init__(self, name: str, hight: int, days: int):
        self.name = name
        self.hight = hight
        self.days = days


def ft_plant_factory():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("oak", 200, 365),
        Plant("fern", 15, 120),
        Plant("dandelions", 12, 200),
        Plant("succulent", 5, 60)
        ]

    i: int = 0
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"crated: {plant.name} ({plant.hight}cm, {plant.days} days old)")
        i += 1
    print(f"Total Plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
