class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0
        self.age = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
a = Plant()


if __name__ == "__main__":
    a = Plant()
    a.name = "Rose"
    a.height = 25
    a.age = 30
    b = Plant()
    b.name = "Sunflower"
    b.height = 80
    b.age = 45
    c = Plant()
    c.name = "Cactus"
    c.height = 15
    c.age = 120
    print("=== Garden Plant Registry ===")
    a.show()
    b.show()
    c.show()
