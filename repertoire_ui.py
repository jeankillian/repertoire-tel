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
from repertoire_action import *
from terminaltables import AsciiTable
print(__doc__)
directory = get_rep()
while True:
    action = input("What type of action would you like to do ? ").upper()
    if action == "A" or action == "L" or action == "D" or action == "Q" or action == "S" or action == "M":
        if action == "A":
            print("You chose the adding contact action")
            contact_name = input("Enter a contact name ").title()
            phone_number = input("Enter a phone number ")
            address = input("Enter an address (city) ")
            ajouter_personne(directory, contact_name, phone_number, address)
            print("-----")
        if action == "L":
            print("List of all registered contact:")
            final_directory = [["contact", "number", "address"]]
            for contact in directory:
                personne = []
                personne.append(contact['name'])
                personne.append(contact['number'])
                personne.append(contact['address'])
                final_directory.append(personne)
            table = AsciiTable(final_directory)
            get_rep()
            print(table.table)
            print("-----")
        if action == "D":
            print("You chose the deleting contact action")
            contact_name = input("Enter the name of the targeted contact ").title()
            supprimer_personne(directory, contact_name)
            print("-----")
        if action == "S":
            print("You chose to search informations for targeted contact")
            contact_name = input("Enter a contact name ").title()
            res = chercher_personnes(directory, contact_name)
            print(res)
            print("-----")
        if action == "M":
            print("You chose to modify informations for targeted contact")
            contact_name = input("Enter a contact name ").title()
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
