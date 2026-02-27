class SecurePlant:

    def __init__(self, name: str, hight: int, days: int):
        self.name = name
        self.hight = hight
        self.days = days

    def set_height(self, hight: int):
        if hight < 0:
            print(f"invalid opperation attempt: height {hight} [REJECTED]")
            print("security: Negativ hieght is Rejected")
        else:
            self.hight = hight
            print(f"Height updated: {hight}cm [OK]")

    def set_age(self, days: int):
        if days < 0:
            print(f"invalid opperation attempt: age {days} [REJECTED]")
            print("Security: Negativ Age is Imposible.. Rejected")
        else:
            self.days = days
            print(f"Age updated: {days} days [OK]")

    def get_height(self):
        return self.hight

    def get_age(self):
        return self.days


def ft_plant_security():
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", 5, 60)
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-42)
    print(f"current plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


if __name__ == "__main__":
    ft_plant_security()
