import csv
import datetime

# Create the file "Menu.txt"
with open("menu.txt", "w") as menu_file:
    menu_file.write("* Please Select a Pizza Base:\n1: Classic\n2: Margarita\n3: TurkPizza\n4: Plain Pizza\n* and the sauce of your choice:\n11: Olive\n12: Mushrooms\n13: Goat Cheese\n14: Meat\n15: Onion\n16: Corn\n* Thank you!")

# Define the Pizza class
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    # Get description of the pizza
    def get_description(self):
        return self.description
    
    # Get cost of the pizza
    def get_cost(self):
        return self.cost

# Define the Decorator class as the superclass of all sauce classes
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost
    
    def get_cost(self):
        return self.component.get_cost() + self.cost
    
    def get_description(self):
        return self.component.get_description() + ' ' + self.description

# Define the toppings as subclasses of Decorator
class Olive(Decorator):
    def __init__(self, component):
        super().__init__(component, "with Olive", 1.50)

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component, "with Mushrooms", 2.00)

class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component, "with Goat Cheese", 2.50)

class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component, "with Meat", 3.00)

class Onion(Decorator):
    def __init__(self, component):
        super().__init__(component, "with Onion", 1.00)

class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component, "with Corn", 1.50)

# Define subclasses of Pizza for different types of pizza
class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 10.99)

class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 12.99)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 14.99)

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 16.99)

# Define a main function to interact with the user and calculate the total price
def main():
    print("Welcome to our pizza shop! Here's our menu:")
    with open("menu.txt", "r") as menu_file:
        print(menu_file.read())
    
    # Select pizza base
    while True:
        base_choice = input("Please select a pizza base (1-4): ")
        if base_choice in ["1", "2", "3", "4"]:
            break
        print("Invalid choice. Please try again.")
    
    # Create pizza object based on user's choice
    if base_choice == "1":
        pizza = Classic()
    elif base_choice == "2":
        pizza = Margarita()
    elif base_choice == "3":
        pizza = TurkPizza()
    else:
        pizza = DominosPizza()
    
    # Select sauce
    while True:
        sauce_choice = input("Please select a sauce (11-16): ")
        if sauce_choice in ["11", "12", "13", "14", "15", "16"]:
            break
        print("Invalid choice. Please try again.")
    
    # Decorate pizza object with selected sauce
    if sauce_choice == "11":
        pizza = Olive(pizza)
    elif sauce_choice == "12":
        pizza = Mushrooms(pizza)
    elif sauce_choice == "13":
        pizza = GoatCheese(pizza)
    elif sauce_choice == "14":
        pizza = Meat(pizza)
    elif sauce_choice == "15":
        pizza = Onion(pizza)
    else:
        pizza = Corn(pizza)
    
    # Calculate total cost
    total_cost = pizza.get_cost()
    
     # Get user's name and ID number
    name = input("Please enter your name: ")
    id_number = input("Please enter your ID number: ")
    credit_card_number = input("Please enter your credit card number: ")
    password = input("Please enter your password: ")
    
    # Print order details
    print()
    print("Order Details:")
    print("Pizza: " + pizza.get_description())
    print("Total cost: $%.2f" % total_cost)
    print("Name: " + name)
    print("ID Number: " + id_number)
    print("Credit Card Number: " + credit_card_number)
    print("Password: " + password)
    
    
    # Save order details to orders.csv file
    with open("orders.csv", "a", newline="") as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow([name, id_number,credit_card_number,password, pizza.get_description(), total_cost, datetime.datetime.now()])
    
    print("Thank you for your order!")
    
if __name__ == "__main__":
    main() 