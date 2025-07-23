import json
import os

# File to store contacts
DATA_FILE = "contacts.json"

# Load existing contacts or create a new file
def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Display all contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!\n")
        return
    print("\n===== CONTACT LIST =====")
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} | {c['phone']} | {c['email']}")
    print("=========================\n")

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("\nContact added successfully!\n")

# Search contacts by name or phone
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]
    if results:
        print("\nSearch Results:")
        for idx, c in enumerate(results, start=1):
            print(f"{idx}. {c['name']} | {c['phone']} | {c['email']}")
    else:
        print("\nNo matching contacts found!\n")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        deleted = contacts.pop(idx)
        save_contacts(contacts)
        print(f"\nDeleted contact: {deleted['name']}\n")
    except (ValueError, IndexError):
        print("\nInvalid contact number!\n")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("""
========= CONTACT BOOK =========
1. View Contacts
2. Add Contact
3. Search Contact
4. Delete Contact
5. Exit
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice! Try again.\n")

if __name__ == "__main__":
    main()
