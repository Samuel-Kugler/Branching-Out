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


def filter_users_by_name(name: str):
    """
    Displays the data of all persons with the name given.
    :param name: str
    """
    users = get_data()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


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


commands = {
    "name": {
        "execute": filter_users_by_name,
        "args": get_name
    }
}


if __name__ == "__main__":
    filter_option = (input(f"What would you like to filter by? (Currently, {commands.keys()} is supported): ").strip()
                     .lower())

    if filter_option in commands.keys():
        commands[filter_option]["execute"](commands[filter_option]["args"]())
    else:
        print("Filtering by that option is not yet supported.")