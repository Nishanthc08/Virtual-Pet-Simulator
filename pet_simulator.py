import random
import time

class Pet:
    def __init__(self, name):
        """Initialize the pet with a name and default attributes."""
        self.name = name
        self.hunger = 50  # Hunger level (0 = full, 100 = starving)
        self.happiness = 50  # Happiness level (0 = sad, 100 = very happy)
        self.health = 100  # Health level (0 = dead, 100 = perfectly healthy)

    def feed(self):
        """Feed the pet to decrease hunger."""
        if self.hunger > 0:
            self.hunger -= 10  # Decrease hunger by 10 units
            if self.hunger < 0:
                self.hunger = 0
            print(f"You fed {self.name}. Hunger level is now {self.hunger}.")
        else:
            print(f"{self.name} is already full!")

    def play(self):
        """Play with the pet to increase happiness."""
        if self.happiness < 100:
            self.happiness += 10  # Increase happiness by 10 units
            if self.happiness > 100:
                self.happiness = 100
            print(f"You played with {self.name}. Happiness level is now {self.happiness}.")
        else:
            print(f"{self.name} is already very happy!")

    def check_health(self):
        """Check the pet's health and adjust it based on hunger and happiness."""
        if self.hunger > 80:
            self.health -= 5  # Decrease health if hunger is high
        elif self.hunger < 20:
            self.health += 5  # Increase health if hunger is low

        if self.happiness < 20:
            self.health -= 5  # Decrease health if happiness is low
        elif self.happiness > 80:
            self.health += 5  # Increase health if happiness is high
        
        # Ensure health stays within bounds
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0

        print(f"{self.name}'s health level is now {self.health}.")

    def is_alive(self):
        """Check if the pet is still alive."""
        return self.health > 0

    def status(self):
        """Display the pet's current status."""
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Health: {self.health}/100")
        print("----------------------------")

def main():
    """Main game loop where the user interacts with the pet."""
    print("Welcome to the Virtual Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    pet = Pet(pet_name)

    while pet.is_alive():
        pet.status()
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Do nothing (time passes)")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            print("Time passes...")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

        # Simulate time passing
        time.sleep(2)
        
        # Increase hunger and decrease happiness, ensuring bounds are respected
        pet.hunger += random.randint(5, 10)  # Hunger increases gradually
        pet.happiness -= random.randint(5, 10)  # Happiness decreases gradually
        
        # Ensure hunger and happiness stay within bounds
        if pet.hunger > 100:
            pet.hunger = 100
        if pet.happiness < 0:
            pet.happiness = 0
        
        pet.check_health()

    print(f"Sadly, {pet.name} has passed away. Game over.")

if __name__ == "__main__":
    main()
