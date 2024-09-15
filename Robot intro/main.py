class Robot:
    def __init__(self, name, battery_level=100, position=(0, 0)):
        self.name = name
        self.battery_level = battery_level
        self.position = position

    def move(self, a, b):
        if self.battery_level > 0:
            self.position = (a, b)
            self.battery_level -= 1  # Decrease battery level for each move
            print(f"{self.name} moved to {self.position}. Battery level: {self.battery_level}")
        else:
            print(f"{self.name} has no battery left!")

    def charge(self):
        self.battery_level = 100
        print(f"{self.name} is fully charged.")

    def introduce(self):
        print(f"Hello, I am {self.name}. My current position is {self.position} and my battery level is {self.battery_level}.")

    def __str__(self):
        return f"Robot(name={self.name}, battery_level={self.battery_level}, position={self.position})"
def main():
    # Create instances of the Robot class
    robot1_name = input("Enter the first robot's name: ")
    robot2_name = input("Enter the second robot's name: ")
    robot1 = Robot(name=robot1_name)
    robot2 = Robot(name=robot2_name)
    
    # Introduce both robots
    robot1.introduce()
    robot2.introduce()
    
    while True:
        # Take user input for commands
        command = input("Enter a command (e.g., move1 x y, move2 x y, charge1, charge2, introduce1, introduce2, or quit): ").strip().lower()
        
        if command.startswith("move1"):
            try:
                _, x, y = command.split()
                x, y = int(x), int(y)
                robot1.move(x, y)
            except ValueError:
                print("Invalid input. Use the format: move1 x y")
        
        elif command.startswith("move2"):
            try:
                _, x, y = command.split()
                x, y = int(x), int(y)
                robot2.move(x, y)
            except ValueError:
                print("Invalid input. Use the format: move2 x y")
        
        elif command == "charge1":
            robot1.charge()
        
        elif command == "charge2":
            robot2.charge()
        
        elif command == "introduce1":
            robot1.introduce()
        
        elif command == "introduce2":
            robot2.introduce()
        
        elif command == "quit":
            print("Exiting...")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

    