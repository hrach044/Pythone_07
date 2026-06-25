class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age
        self.stats = Plant.Stats()
        self.growht = 8.0
        self.age_growht = 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")
        self.stats.show_count += 1

    def grow(self) -> None:
        self.height += self.growht
        self.stats.grow_count += 1

    def age(self) -> None:
        self.days += self.age_growht
        self.stats.age_count += 1

    @staticmethod
    def is_older(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, "
                  f"{self.show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def grow(self) -> None:
        super().grow()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0
        self.growht = 30.0
        self.age_growht = 20

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.Stats = Tree.Stats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats.shade_count += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade_count} shade")


def display_stats(plant: Plant) -> None:
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older(400)}")
    print("=== Flower")
    a = Flower("Rose", 15.0, 10, "red")
    a.show()
    print(f"[statistics for {a.name}]")
    display_stats(a)
    print(f"[asking the {a.name} to grow and bloom]")
    a.bloom()
    a.grow()
    a.show()
    print(f"[statistics for {a.name}]")
    display_stats(a)
    print("\n")

    print("=== Tree")
    b = Tree("Oak", 200.0, 365, 5.0)
    b.show()
    print(f"[statistics for {b.name}]")
    display_stats(b)
    print("[asking the oak to produce shade]")
    b.produce_shade()
    print(f"[statistics for {b.name}]")
    display_stats(b)
    print("\n")

    print("=== Seed")
    c = Seed("Sunflower", 80.0, 45, "yellow")
    c.show()
    print(f"[make {c.name} grow, age and bloom]")
    c.bloom()
    c.age()
    c.grow()
    c.show()
    print(f"[statistics for {c.name}]")
    display_stats(c)

    print("\n")
    print("=== Anonymous")
    d = Plant.anonymous()
    d.show()
    print("[statistics for Unknown plant]")
    display_stats(d)
