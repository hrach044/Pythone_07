import typing
import random

players = ['alice', 'bob', 'charlie', 'dylan', 'emma', 'frank',
           'grace', 'henry', 'isabel', 'jack', 'karen', 'liam',
           'mia', 'noah', 'olivia', 'peter']

actions = ['run', 'jump', 'swim', 'climb', 'grab', 'move', 'sleep',
           'eat', 'use', 'release', 'attack', 'defend', 'craft',
           'build', 'explore', 'trade', 'heal', 'fly', 'hide',
           'cast', 'dash', 'block', 'dodge', 'sprint',
           'sneak', 'shoot', 'reload', 'loot', 'revive',
           'teleport', 'summon', 'enchant', 'mine', 'fish',
           'cook', 'brew', 'ride', 'tame', 'unlock',
           'hack', 'scan', 'charge', 'shield', 'parry',
           'roll', 'vault', 'glide']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple[str, str]]) -> \
                          typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield (event)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generatore = gen_event()
    for i in range(0, 1000):
        event = next(generatore)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events: list[tuple[str, str]] = []
    for i in range(0, 10):
        event = next(generatore)
        events.append(event)
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
