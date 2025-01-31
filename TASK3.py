class ContactBook:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"\nName: {name}")
                for key, value in details.items():
                    print(f"{key}: {value}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"\nDetails for {name}:")
            for key, value in self.contacts[name].items():
                print(f"{key}: {value}")
        else:
            print(f"Contact {name} not found.")

    def update_contact(self, name):
        if name in self.contacts:
            print(f"Updating details for {name}:")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ").title()
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == "2":
            contact_book.view_contacts()
        
        elif choice == "3":
            name = input("Enter the name to search: ").title()
            contact_book.search_contact(name)
        
        elif choice == "4":
            name = input("Enter the name to update: ")
            contact_book.update_contact(name)
        
        elif choice == "5":
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == "6":
            print("Exiting Contact Book. Thankyou...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
