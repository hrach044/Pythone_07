class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def plant_check(name: str) -> None:
    raise PlantError(f"The {name} plant is wilting!")


def water_check(amount: int) -> None:
    raise WaterError("Not enough water in the tank!")


def error_check() -> None:
    try:
        print("Testing PlantError...")
        plant_check("tomato")
    except PlantError as e:
        print(f"Cought PlantError: {e}", end="\n\n")
    try:
        print("Testing WaterError...")
        water_check(6)
    except WaterError as e:
        print(f"Caught WaterError: {e}", end="\n\n")
    try:
        print("Testing catching all garden errors...")
        plant_check("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        water_check(6)
    except GardenError as e:
        print(f"Caught GardenError: {e}", end="\n\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===", end="\n\n")
    error_check()
    print("All custom error types work correctly!")
