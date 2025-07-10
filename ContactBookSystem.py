
contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact '{name}' added.")
        
    elif choice == '2':
        if contacts:
            print("\n Contact List:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("Contact book is empty.")
            
    elif choice == '3':
        print("Bye!")
        break
        
    else:
        print("Invalid choice. Try again.")
