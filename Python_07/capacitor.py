from ex1 import (CreatureFactory, HealingCreatureFactory,
                 TransformCreatureFactory)
from ex1.capabilities import HealCapability, TransformCapability


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    assert isinstance(base, HealCapability)
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    assert isinstance(evolved, HealCapability)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())
    print()


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    assert isinstance(base, TransformCapability)
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    assert isinstance(evolved, TransformCapability)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


test_healing(HealingCreatureFactory())
test_transform(TransformCreatureFactory())
