class Plant:

    def __init__(self, name: str, hight: int, age: int):
        self.name = name
        self.hight = hight
        self.age = age


def ft_garden_data():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Refistery ===")
    print(f"{plant1.name}: {plant1.hight}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.hight}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.hight}cm, {plant3.age} days old")


if __name__ == "__main__":
    ft_garden_data()
