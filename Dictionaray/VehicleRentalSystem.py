class Vehicle:
    def __init__(self, name, model, rent_per_day):
        self.name = name
        self.model = model
        self.rent_per_day = rent_per_day

    def get_type(self):
        return "General Vehicle"

    def display_info(self):
        print(f"{self.get_type()} - {self.name} ({self.model}) | Rent: {self.rent_per_day} Taka/day")


class Bus(Vehicle):
    def get_type(self):
        return "Bus"


class Motorcycle(Vehicle):
    def get_type(self):
        return "Motorcycle"


class Customer:
    def __init__(self, name, nid):
        self.__name = name
        self.__nid = nid

    def get_info(self):
        return f"Customer: {self.__name}, NID: {self.__nid}"


# Sample vehicles
vehicles = [
    Bus("Green Line", "Volvo", 5000),
    Motorcycle("Yamaha", "FZ", 800),
    Bus("Hanif", "Hino", 4500),
    Motorcycle("Honda", "CBR", 900)
]

# Main Program
while True:
    print("\n=== Vehicle Rental System ===")
    print("1. Show All Vehicles")
    print("2. Rent a Vehicle")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nAvailable Vehicles:")
        for v in vehicles:
            v.display_info()

    elif choice == '2':
        name = input("Enter your name: ")
        nid = input("Enter your NID: ")
        customer = Customer(name, nid)

        print("\nSelect a vehicle:")
        for idx, v in enumerate(vehicles):
            print(f"{idx + 1}. {v.get_type()} - {v.name} ({v.model})")

        try:
            select = int(input("Select vehicle number to rent: ")) - 1
            days = int(input("How many days to rent?: "))
            selected = vehicles[select]

            print("\n Rental Receipt:")
            print(customer.get_info())
            print(f"Vehicle: {selected.name} ({selected.model})")
            print(f"Total Rent: {selected.rent_per_day * days} Taka")

        except (IndexError, ValueError):
            print(" Invalid selection. Please try again.")

    elif choice == '3':
        print("Thanks for using our system.")
        break

    else:
        print("Invalid choice.")
