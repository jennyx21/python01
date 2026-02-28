class Plant:

    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.hight = height
        self.days = days
        
    def set_age(self, days: int):
        if days < 0:
            print(f"invalid opperation attempt: age {days} [REJECTED]")
            print("Security: Negativ Age is Imposible.. Rejected")
        else:
            self.days = days

    def set_height(self, hight: int):
        if hight < 0:
            print(f"invalid opperation attempt: height {hight} [REJECTED]")
            print("security: Negativ hieght is Rejected")
        else:
            self.hight = hight


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str):
        super.__init__(name, height, days)
        self.color = color

    def get_info(self):
        return f"{self.name}(Flower): {self.hight}cm, {self.days} days old, {self.color} color"


class Tree(Plant):
    def __init__ (self, name: str, height: int, days: int, trunk_diameter: int):
        super.__init__ (name, height, days)
        self.trunk_diameter = trunk_diameter
    def get_info(self):
        return f"{self.name}(Tree): {self.hight}cm, {self.days} days old, {self.trunk_diameter}cm diameter"


class Vegteble(Plant):
    def __init__ (self, name: str, height: int, days: int, harvest_season: str, nutritional_value: str):
        super.__init__ (name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def get_info(self):
        return (f"{self.name}(Vegetable): {self.hight}cm, {self.days} days old, {self.harvest_season} harvest\n"
                f"")
    