import repertoire_utils_text as repertoire_utils


def index_fun(directory, contact_name):
    for i in directory:
        if i["name"] == contact_name:
            return directory.index(i)
    return -1


def ajouter_personne(directory, contact_name=None, phone_number=None, address=None):
    if index_fun(directory, contact_name) == -1:
        personne = {}
        personne["name"] = contact_name
        personne["number"] = phone_number
        personne["address"] = address
        repertoire_utils.append_rep(directory, personne)
        print(contact_name + " added")


def get_rep():
    return repertoire_utils.get_rep()


def supprimer_personne(directory, contact_name):
    personnes = chercher_personnes(directory, contact_name=contact_name)
    if personnes:
        for personne in personnes:
            repertoire_utils.del_rep(directory, personne)
        print(contact_name + " deleted")


def chercher_personnes(directory, contact_name=None, phone_number=None, address=None):
    """function : search informations with the contact name in the directory"""
    res = []
    for contact in directory:
        dir_name = contact['name']
        dir_address = contact['address']
        dir_phone = contact['number']
        if contact_name and (contact_name in dir_name) or \
                address and (address in dir_address) or \
                phone_number and (phone_number in dir_phone):
            res.append(contact)
    return res


def modify_phone_number_of_contact(directory, contact_name):
    """function : modify the number of a contact in the directory"""
    for contact in directory:
        if contact['name'] == contact_name:
            contact['number'] = input("Enter a new phone number ")
            print("The phone number of " + contact_name + " has changed!")
            break
        else:
            print("\033[31m...\033[0m")
    repertoire_utils.write_dir(directory)


def modify_address_of_contact(directory, contact_name):
    """function : modify the address of a contact in the directory"""
    for contact in directory:
        if contact['name'] == contact_name:
            contact['address'] = input("Enter a new address ")
            print("The address of " + contact_name + " has changed!")
            break
        else:
            print("\033[31m...\033[0m")
    repertoire_utils.write_dir(directory)
