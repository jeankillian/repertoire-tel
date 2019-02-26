"""
    ####################################################################
                   <--Welcome to your phone directory-->

       List of available action:
       A: Adding contact to the directory
       L: Listing all added contact in the directory
       D: Deleting targeted contact from directory
       Q: Exit phone directory
       S: Search phone number with the contact name in the directory
       M(p): Modify the number of a contact in the directory
       M(a): Modify the address of a contact in the directory

    ####################################################################
"""
from repertoire_action2 import *
directory = []
first_log = True
print(__doc__)
while True:
    action = input("What type of action would you like to do ? ").upper()
    if action == "A" or action == "L" or action == "D" or action == "Q" or action == "S" or action == "M":
        if action == "A":
            print("You chose the adding contact action")
            contact_name = input("Enter a contact name ").upper()
            phone_number = input("Enter a phone number ")
            address = input("Enter an address (city) ")
            create_contact(directory, contact_name, phone_number, address, first_log)
            print("-----")
        if action == "L":
            list_of_contact(directory)
            print("-----")
        if action == "D":
            print("You chose the deleting contact action")
            contact_name = input("Enter the name of the targeted contact ").upper()
            delete_contact(directory, contact_name)
            print("-----")
        if action == "S":
            print("You chose to search phone number for targeted contact")
            contact_name = input("Enter a contact name ").upper()
            search_phone_number_of_contact(directory, contact_name)
            print("-----")
        if action == "M":
            print("You chose to modify informations for targeted contact")
            contact_name = input("Enter a contact name ").upper()
            action_of_modify = input("Press 'p' to modify phone number or 'a' to modify address ").lower()
            if action_of_modify == "p":
                modify_phone_number_of_contact(directory, contact_name)
            if action_of_modify == "a":
                modify_address_of_contact(directory, contact_name)
            print("-----")
        if action == "Q":
            print("\033[33mBye Bye !\033[0m")
            break
    else:
        print("\033[31mERROR: Available actions: A, L, D, Q, R, M(a, p) !\033[0m")
