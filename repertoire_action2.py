# from terminaltables import AsciiTable
def create_contact(directory, contact_name, phone_number, address):
    """function : adding contact to the directory"""
    temp_directory = {}
    temp_directory["contact"] = contact_name
    temp_directory["number"] = phone_number
    temp_directory["address"] = address
    directory.append(temp_directory)
    print("Contact", contact_name, "added !")


def list_of_contact(directory):
    """function : listing all added contact in the directory"""
    print("List of all registered contact:")
    final_directory = [["contact", "number", "address"]]
    for i, elt in enumerate(directory):
        temp_directory = []
        temp_directory.append(elt['contact'])
        temp_directory.append(elt['number'])
        temp_directory.append(elt['address'])
        final_directory.append(temp_directory)
    print(final_directory)
    # table = AsciiTable(final_directory)
    # print(table.table)


def delete_contact(directory, contact_name):
    """function : deleting targeted contact from directory"""
    for i in range(len(directory)):
        if contact_name in directory[i].values():
            directory.pop(i)
            print("Contact", contact_name, "deleted !")
            break
        else:
            print("\033[31m...\033[0m")


def search_phone_number_of_contact(directory, contact_name):
    """function : search informations with the contact name in the directory"""
    for i in range(len(directory)):
        if contact_name in directory[i].values():
            number = directory[i]['number']
            address = directory[i]['address']
            print("The phone number of " + contact_name + " is '" + number + "' and its address is '" + address + "'")
            break
        else:
            print("\033[31mThe contact you're looking for does not exist !\033[0m")


def modify_phone_number_of_contact(directory, contact_name):
    """function : modify the number of a contact in the directory"""
    for i in range(len(directory)):
        if contact_name in directory[i].values():
            directory[i]['number'] = input("Enter a new phone number ")
            print("The phone number of " + contact_name + " has changed!")
            break
        else:
            print("\033[31m...\033[0m")


def modify_address_of_contact(directory, contact_name):
    """function : modify the address of a contact in the directory"""
    for i in range(len(directory)):
        if contact_name in directory[i].values():
            directory[i]['address'] = input("Enter a new address ")
            print("The address of " + contact_name + " has changed!")
            break
        else:
            print("\033[31m...\033[0m")
