import random

big = ['Boss Slayer', 'Speed Runner', 'Untouchable', 'Master Explorer',
       'Collector Supreme', 'World Savior', 'Crafting Genius', 'Strategist',
       'Unstoppable', 'Survivor', 'Treasure Hunter', 'First Steps',
       'Sharp Mind', 'Hidden Path Finder']


def gen_player_achievements() -> set[str]:
    k = random.randint(7, 9)
    mini = random.sample(big, k)
    s = set(mini)
    return s


if __name__ == "__main__":
    print("=== Achievement Tracker System ===", end="\n\n")
    players = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements()}
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}", end="\n\n")
    distinct = players['Alice'].union(players['Bob'],
                                      players['Charlie'],
                                      players['Dylan'])
    print(f"All distinct achievements: {distinct}", end="\n\n")
    common = players['Alice'].intersection(players['Bob'],
                                           players['Charlie'],
                                           players['Dylan'])
    print(f"Common achievements: {common}", end="\n\n")
    for name, achievements in players.items():
        other: set[str] = set()
        for other_name, other_achievements in players.items():
            if name != other_name:
                other = other.union(other_achievements)
        print(f"Only {name} has: {achievements.difference(other)}")
    print("\n")
    for name, achievements in players.items():
        print(f"{name} is missing: {set(big).difference(achievements)}")
