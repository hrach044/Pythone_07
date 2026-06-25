import math


def get_player_pos() -> tuple[float, float, float]:
    answer = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        a, b, c = answer.split(",")
    except ValueError:
        print("Invalid syntax")
        return get_player_pos()
    try:
        x = float(a)
    except ValueError as e:
        print(f"Error on parameter '{a}': {e}")
        return get_player_pos()
    try:
        y = float(b)
    except ValueError as e:
        print(f"Error on parameter '{b}': {e}")
        return get_player_pos()
    try:
        z = float(c)
    except ValueError as e:
        print(f"Error on parameter '{c}': {e}")
        return get_player_pos()
    return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===", end="\n\n")
    print("Get a first set of coordinates")
    cord = get_player_pos()
    print(f"Got a first tuple: {cord}")
    x1 = cord[0]
    y1 = cord[1]
    z1 = cord[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    centr = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(centr, 4)}", end="\n\n")
    print("Get a second set of coordinates")
    cord = get_player_pos()
    x2 = cord[0]
    y2 = cord[1]
    z2 = cord[2]
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(result, 4)}")
