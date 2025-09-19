class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("pet_type must be one of PET_TYPES")
        self.name = name
        self._owner = None
        self.owner = owner  # через сеттер (проверка типа)
        self.pet_type = pet_type
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Owner):
            raise Exception("owner must be an Owner or None")
        self._owner = value


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [p for p in Pet.all if p.owner is self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be a Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda p: p.name)
    