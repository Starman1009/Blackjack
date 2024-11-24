import os

class Human:
    def __init__(self, name, race, age):
        self.name = name
        self.race = race.lower()  # Convert race to lowercase
        self.age = age

    def hello(self):
        if self.race == "white":
            print("Hi")
        if self.race == "latino":
            print(f"{self.name} is also latino!")
        print(f"hello! {self.race} and {self.age}")

class American(Human):
    def __init__(self, name, race, age, state):
        super().__init__(name, race, age)
        self.state = state

    def america(self):
        print(f"and he is from {self.state}")

def get_user_input():
    valid_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    name = input("Enter name: ").strip()  # Remove leading/trailing whitespace
    race = input("Enter race: ").strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
    age = int(input("Enter age: ").strip())  # Remove leading/trailing whitespace
    
    is_american = input("Are you American? Type [Y] or [N]: ").strip().upper()
    state = None
    if is_american == 'Y':
        while True:
            state = input("Enter state (acronym): ").strip().upper()
            if state in valid_states:
                break
            else:
                print("Invalid state acronym. Please enter a valid state acronym (e.g., FL, GA).")
    
    return name, race, age, state

name, race, age, state = get_user_input()

# Clear the terminal screen
if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For Unix-based systems
    os.system('clear')

if state:
    person = American(name, race, age, state)
else:
    person = Human(name, race, age)

person.hello()
if isinstance(person, American):
    person.america()