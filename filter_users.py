import json
from json import JSONDecodeError


def get_data() -> list:
    """
    Loads all the data from a json-file and returns its data
    :return: list
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        return users
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []


def get_name() -> str:
    """
    Gets a valid name and returns it.
    :return: str
    """
    while True:
        name = input("Enter a name to filter users: ").strip()

        if not name.isalpha():
            print(f"{name} is not a valid name! Only letters are valid.")
            continue

        return name


def filter_users_by_name():
    """
    Displays the data of all persons with the name given.
    """
    users = get_data()
    name = get_name()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def get_options() -> str:
    """
    Gets all the command options.
    :return: str
    """
    options = ""
    for key in commands.keys():
        options += key + ", "

    return options[:-2]


commands = {
    "name": filter_users_by_name
}


if __name__ == "__main__":
    filter_option = (input(f"What would you like to filter by? (Currently, {get_options()} is supported): ").strip()
                     .lower())

    if filter_option in commands.keys():
        commands[filter_option]()
    else:
        print("Filtering by that option is not yet supported.")