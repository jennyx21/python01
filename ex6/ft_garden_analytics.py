
class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self, days: int):
        self.height += days
        print(f"{self.name} grew {days}cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.days} days old"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color

    def display_info(self):
        print(f"{self.name}: {self.height}cm, {self.color} flower (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 days: int, color: str, points: int):
        super().__init__(name, height, days, color)
        self.points = points

    def diplay_info(self):
        print(f"{self.name}: {self.height}cm, {self.color} flower (blooming)")
