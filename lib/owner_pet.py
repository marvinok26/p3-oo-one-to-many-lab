class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


# Example usage:
owner1 = Owner("Alice")
owner2 = Owner("Bob")

pet1 = Pet("Fido", "dog", owner1)
pet2 = Pet("Fluffy", "cat", owner1)
pet3 = Pet("Tweety", "bird", owner2)

owner1.add_pet(pet3)  # This should raise an exception since pet3 already has an owner.

sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


# Example usage:
owner1 = Owner("Alice")
owner2 = Owner("Bob")

pet1 = Pet("Fido", "dog", owner1)
pet2 = Pet("Fluffy", "cat", owner1)
pet3 = Pet("Tweety", "bird", owner2)

owner1.add_pet(pet3)  # This should raise an exception since pet3 already has an owner.

sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


# Example usage:
owner1 = Owner("Alice")
owner2 = Owner("Bob")

pet1 = Pet("Fido", "dog", owner1)
pet2 = Pet("Fluffy", "cat", owner1)
pet3 = Pet("Tweety", "bird", owner2)

owner1.add_pet(pet3)  # This should raise an exception since pet3 already has an owner.

sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


# Example usage:
owner1 = Owner("Alice")
owner2 = Owner("Bob")

pet1 = Pet("Fido", "dog", owner1)
pet2 = Pet("Fluffy", "cat", owner1)
pet3 = Pet("Tweety", "bird", owner2)

owner1.add_pet(pet3)  # This should raise an exception since pet3 already has an owner.

sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


# Example usage:
owner1 = Owner("Alice")
owner2 = Owner("Bob")

pet1 = Pet("Fido", "dog", owner1)
pet2 = Pet("Fluffy", "cat", owner1)
pet3 = Pet("Tweety", "bird", owner2)

owner1.add_pet(pet3)  # This should raise an exception since pet3 already has an owner.

sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(pet.name)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
