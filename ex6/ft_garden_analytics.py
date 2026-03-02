class Plant:

    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self, days: int):
        self.hight += days

    def get_info(self):
        return f"{self.name}: {self.hight}cm, {self.days} days old"


class FloweringPlant(Plant):
    def __inti__(self ):

# class Flower(Plant):
#     def __init__(self, name: str, height: int, days: int, color: str):
#         super().__init__(name, height, days)
#         self.color = color

#     def get_info(self):
#         return (f"{self.name} (Flower): {self.height}cm, {self.days} days "
#                 f"old, {self.color} color")

#     def bloom(self):
#         print(f"{self.name} is blooming beautifully!")


# class Tree(Plant):
#     def __init__(self, name: str, height: int, days: int, trunk_diameter: int):
#         super().__init__(name, height, days)
#         self.trunk_diameter = trunk_diameter

#     def produce_shade(self):
#         print(f"{self.name} provides {self.trunk_diameter * 1.56:.0f} "
#               f"square meters of shade")

#     def get_info(self):
#         return (f"{self.name} (Tree): {self.height}cm, {self.days} days old,"
#                 f" {self.trunk_diameter}cm diameter")


# class Vegteble(Plant):
#     def __init__(self, name: str, height: int, days: int, harvest_season: str,
#                  nutritional_value: str):
#         super().__init__(name, height, days)
#         self.harvest_season = harvest_season
#         self.nutritional_value = nutritional_value

#     def get_info(self):
#         return (f"{self.name} (Vegetable): {self.height}cm, {self.days}"
#                 f" days old, {self.harvest_season} harvest")