
class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # in ml
        self.milk = 500  # in ml
        self.coffee_beans = 200  # in grams
        self.cups = 10

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Cups: {self.cups}")

    def make_coffee(self, water_needed, milk_needed, beans_needed):
        if self.water >= water_needed and self.milk >= milk_needed and self.coffee_beans >= beans_needed and self.cups > 0:
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= beans_needed
            self.cups -= 1
            print("Here is your coffee! ☕")
        else:
            print("Sorry, not enough resources to make coffee.")

    def refill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += beans
        self.cups += cups
        print("Machine refilled!")


# Example usage
machine = CoffeeMachine()
machine.report()
machine.make_coffee(200, 50, 15)
machine.report()
machine.refill(500, 200, 100, 5)
machine.report()
