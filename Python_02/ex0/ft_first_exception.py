def input_temperature(temp_str: str) -> int | None:
    try:
        return int(temp_str)
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


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
