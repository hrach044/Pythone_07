import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{sys.argv[1]}'")
            ft: typing.IO[str] = open(sys.argv[1])
            content = ft.read()
            print("---", end="\n\n")
            print(content)
            print("---")
            ft.close()
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
