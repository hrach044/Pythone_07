import sys
import os
import site


def is_virtual() -> bool:
    return sys.prefix != sys.base_prefix


def get_name() -> str:
    if is_virtual():
        return os.path.basename(sys.prefix)
    return ("None detected")


def get_package() -> str:
    paths = site.getsitepackages()
    return paths[0]


def main() -> None:
    if not is_virtual():
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_name()}")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_name()}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(f"{get_package()}")


if __name__ == "__main__":
    main()
