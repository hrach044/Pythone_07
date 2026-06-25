class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        if height > 0:
            self._height = height
        if age > 0:
            self._age = age
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self._name}: {round(self.get_height(), 1)}cm, "
              f"{self.get_age()} days old")

    def result(self) -> None:
        print("Current state: ", end="")
        self.show()

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {round(self.get_height())}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    a = Plant("Rose", 15.0, 10)
    a.set_height(25)
    a.set_age(30)
    a.set_height(-2)
    a.set_age(-2)
    a.result()
