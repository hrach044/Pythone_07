from ex0.factories import CreatureFactory
from . import creature
from ex0.creature import Creature


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return creature.Sproutling()

    def create_evolved(self) -> Creature:
        return creature.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return creature.Shiftling()

    def create_evolved(self) -> Creature:
        return creature.Morphagon()
