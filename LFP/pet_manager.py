class Pet:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.type = "Gato"
        self.state = "Vivo"

    def run(self, distance):
        self.energy -= distance / 2

    def eat(self, weight):
        self.energy += 12 + weight

    def play(self, time):
        self.energy -= time * 0.1

    def summary(self):
        return f"{self.name}, Energía: {int(self.energy)}, {self.type}, {self.state}"

class PetManager:
    def __init__(self):
        self.pets = {}

    def create_pet(self, name):
        self.pets[name] = Pet(name)

    def feed_pet(self, name, weight):
        if name in self.pets:
            self.pets[name].eat(weight)
            return True
        return False

    def play_with_pet(self, name, time):
        if name in self.pets:
            self.pets[name].play(time)
            return True
        return False

    def get_pet_summary(self, name):
        if name in self.pets:
            return self.pets[name].summary()
        return None

    def get_global_summary(self):
        summary = []
        for name, pet in self.pets.items():
            summary.append(pet.summary())
        return summary