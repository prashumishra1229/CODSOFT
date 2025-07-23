import json
import os
import re
import csv

DATA_FILE = "contacts.json"

# Colors for terminal output
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


# ---------------- Contact Class ---------------- #
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}


# ---------------- ContactBook Class ---------------- #
class ContactBook:
    def __init__(self):
        self.contacts = self.load_contacts()

    # Load and Save
    def load_contacts(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def save_contacts(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.contacts, f, indent=4)

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print(f"{Colors.WARNING}No contacts found!{Colors.ENDC}")
            return
        print(f"\n{Colors.OKBLUE}{Colors.BOLD}===== Contact List ====={Colors.ENDC}")
        for idx, c in enumerate(self.contacts, start=1):
            print(f"{idx}. {c['name']} | {c['phone']} | {c['email']}")
        print(f"{Colors.OKBLUE}========================{Colors.ENDC}\n")

    # Add contact
    def add_contact(self):
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone (10 digits): ").strip()
        email = input("Enter Email: ").strip()

        # Validation
        if not re.fullmatch(r"\d{10}", phone):
            print(f"{Colors.FAIL}Invalid phone number! Must be 10 digits.{Colors.ENDC}")
