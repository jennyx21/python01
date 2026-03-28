class SecurePlant:

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        if days < 0:
            print("Error: initial age can't be negative")
            self.days = 0
        else:
            self.days = days
        if height < 0:
            print("Error: initial height can't be negative")
            self.height = 0
        else:
            self.height = height

    def show(self):
        print(f"Plant created: {self.name}: {round(self.height, 1)}cm, "
              f"{self.days} days old \n")

    def set_height(self, height: float):
        if height < 0:
            print("Error: Height can't be negative")
            print("security: Height update rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm")

    def set_age(self, days: int):
        if days < 0:
            print("Error: Age can't be negative")
            print("Security: Age update rejected")
        else:
            self.days = days
            print(f"Age updated: {days} days")

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.days


def ft_plant_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 5, 60)
    rose.show()
    rose.set_height(25.9)
    rose.set_age(30)
    print()
    rose.set_height(-42)
    rose.set_height(-9)
    print()
    print(f"current state: {rose.name} {round(rose.get_height())}cm, "
          f"{rose.get_age()} days old")


if __name__ == "__main__":
    ft_plant_security()
