class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True
        print(f"[asking the {self.name.lower()} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        self.height = self.height + 2.1

    def age(self) -> None:
        self.days = self.days + 1
        self.nutritional_value = self.nutritional_value + 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    a = Flower("Rose", 15.0, 10, "red")
    a.show()
    a.bloom()
    a.show()
    print("=== Tree")
    b = Tree("Oak", 200.0, 365, 5.0)
    b.show()
    b.produce_shade()
    print("=== Vegetable")
    c = Vegetable("Tomato", 5.0, 10, "April", 0)
    c.show()
    print(f"[make {c.name.lower()} grow and age for 20 days]")
    for i in range(1, 21):
        c.age()
        c.grow()
    c.show()
