def input_temperature(temp_str: str) -> int | None:
    try:
        a: int = int(temp_str)
        if a < 0:
            raise ValueError(f"{a}°C is too cold for plants (min 0°C)")
        if a > 40:
            raise ValueError(f"{a}°C is too hot for plants (max 40°C)")
        return a
    except ValueError as e:
        print(f"Caught input_temperature error: {e}", end="\n\n")
        return None


def test_temperature() -> None:
    print("Input data is '25'")
    a = input_temperature("25")
    if a is not None:
        print(f"Temperature is now {a}°C", end="\n\n")
    print("Input data is 'abc'")
    a = input_temperature("abc")
    if a is not None:
        print(f"Temperature is now {a}°C", end="\n\n")
    print("Input data is '100'")
    a = input_temperature("100")
    if a is not None:
        print(f"Temperature is now {a}°C", end="\n\n")
    print("Input data is '-50'")
    a = input_temperature("-50")
    if a is not None:
        print(f"Temperature is now {a}°C", end="\n\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
