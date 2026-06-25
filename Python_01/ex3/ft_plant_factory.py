class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def create(self) -> None:
        print("Created: ", end="")
        self.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    a = Plant("Rose", 25.0, 30)
    a.create()
    b = Plant("Oak", 200.0, 365)
    b.create()
    c = Plant("Cactus", 5.0, 90)
    c.create()
    d = Plant("Sunflower", 80.0, 45)
    d.create()
    e = Plant("Fern", 15.0, 120)
    e.create()
