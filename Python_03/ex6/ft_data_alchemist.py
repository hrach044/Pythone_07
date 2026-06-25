import random


names = ['Alice', 'bob', 'Charlie', 'dylan',
         'Emma', 'Gregory', 'john', 'kevin', 'Liam']


if __name__ == "__main__":
    print("=== Game Data Alchemist ===", end="\n\n")
    print(f"Initial list of players: {names}")

    capitalized = [name.capitalize() for name in names]
    print(f"New list with all names capitalized: {capitalized}")

    upper = [name for name in names if name == name.capitalize()]
    print(f"New list of capitalized names only: {upper}", end="\n\n")

    scores = {name: random.randint(1, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    average = round(float(sum(scores.values()) / len(scores)), 2)
    print(f"Score average is {average}")

    higher = {name: value for name, value in scores.items() if value > average}
    print(f"High scores: {higher}")
