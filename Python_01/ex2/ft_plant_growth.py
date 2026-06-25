class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0.0
        self.days = 0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.days = self.days + 1
a = Plant()


if __name__ == "__main__":
    a = Plant()
    a.name = "Rose"
    a.height = 25.0
    a.days = 30
    print("=== Garden Plant Growth ===")
    a.show()
    start = a.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        a.grow()
        a.age()
        a.show()
    total = a.height - start
    print(f"Growth this week: {round(total, 1)}cm")
