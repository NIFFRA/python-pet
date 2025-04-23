class Pet:
    def __init__(self, name):
        """Initialize the pet with a name and default attribute values."""
        self.name = name
        self.hunger = 5  # Scale from 0 (full) to 10 (very hungry)
        self.energy = 5  # Scale from 0 (tired) to 10 (fully rested)
        self.happiness = 5  # Scale from 0 to 10
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """Reduces hunger and increases happiness."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate and feels satisfied!")

    def sleep(self):
        """Increases energy."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept and feels well-rested!")

    def play(self):
        """Reduces energy, increases happiness, and slightly increases hunger."""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and had fun!")

    def get_status(self):
        """Displays the current attributes of the pet."""
        print(f"{self.name}'s Status - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

    def train(self, trick):
        """Teaches a new trick to the pet."""
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """Displays the tricks the pet has learned."""
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")
