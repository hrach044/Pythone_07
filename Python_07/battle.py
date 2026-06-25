from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


test_factory(FlameFactory())
test_factory(AquaFactory())
test_battle(FlameFactory(), AquaFactory())
