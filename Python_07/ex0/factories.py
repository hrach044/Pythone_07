from abc import ABC, abstractmethod
from . import creature


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> creature.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> creature.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        return creature.Flameling()

    def create_evolved(self) -> creature.Creature:
        return creature.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        return creature.Aquabub()

    def create_evolved(self) -> creature.Creature:
        return creature.Torragon()
