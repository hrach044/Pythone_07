def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2 / 0
    elif operation_number == 2:
        open("non/existent/file")
    elif operation_number == 3:
        "hello" + 5
    else:
        return


def test_error_types() -> None:
    try:
        print("Testing operation 0...")
        garden_operations(0)
        print("Operation completed successfully", end="\n\n")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print("Testing operation 1...")
        garden_operations(1)
        print("Operation completed successfully", end="\n\n")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print("Testing operation 2...")
        garden_operations(2)
        print("Operation completed successfully", end="\n\n")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print("Testing operation 3...")
        garden_operations(3)
        print("Operation completed successfully", end="\n\n")
    except (ValueError, ZeroDivisionError,  FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print("Testing operation 4...")
        garden_operations(4)
        print("Operation completed successfully", end="\n\n")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden  Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")
