import json


def index_fun(directory, contact_name):
    for contact in directory:
        if contact["name"] == contact_name:
            return directory.index(contact)
    return -1


def append_rep(directory, personne):
    directory.append(personne)
    write_dir(directory)


def get_rep():
    """function : listing all added contact in the directory"""
    with open("data.json", "r") as fichier:
        test = fichier.read()
        if test:
            directory = json.loads(test)
        else:
            directory = []
        return directory


def del_rep(directory, personne):
    """function : deleting targeted contact from directory"""
    directory.remove(personne)
    write_dir(directory)


def write_dir(directory):
    with open("data.json", "w") as fichier:
        fichier.write(json.dumps(directory, indent=4))
