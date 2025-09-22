import json
from json import JSONDecodeError


#Possible Mail Providers
possible_mail_providers = ["@example.com"]


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
        return [{"id": 0, "name": "test", "age": -1, "email": "test@example.com"}]
    except JSONDecodeError:
        return [{"id": 0, "name": "test", "age": -1, "email": "test@example.com"}]


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

    if len(filtered_users) == 0:
        print("No user met the criteria!")
        return

    for user in filtered_users:
        print(user)


def get_age() -> int:
    """
    Gets the age
    :return: int
    """
    while True:
        age = input("Enter a age you want to filter users: ").strip()

        if not age.isdigit():
            print(f"{age} is not a valid input! Only positive Integers are valid.")
            continue

        age = int(age)
        MAX_AGE = 130

        if age > MAX_AGE:
            print(f"{age} is not a possible age, please enter age between 0 and {MAX_AGE}!")
            continue

        return age


def filter_users_by_age():
    """
       Displays the data of all persons with the age given.
       """
    users = get_data()
    age = get_age()

    filtered_users = [user for user in users if user["age"] == age]

    if len(filtered_users) == 0:
        print("No user met the criteria!")
        return

    for user in filtered_users:
        print(user)


def get_email() -> str:
    """
    Gets a valid email from the user.
    :return: str
    """
    while True:
        email = input("Please enter the email of the student: ").strip()

        position_mail_prefix = email.find("@")

        if not email[position_mail_prefix:] in possible_mail_providers:
            print(f"{email} is not a valid email! Possible emails end with: {possible_mail_providers}")
            continue

        return email


def filter_users_by_email():
    """
    Displays the user with the correct email.
    """
    users = get_data()
    email = get_email()
    filtered_user = None

    for user in users:
        if user["email"] == email:
            filtered_user = user
            break

    if filtered_user is None:
        print("No user for this email!")
        return

    print(filtered_user)


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
    "name": filter_users_by_name,
    "age": filter_users_by_age,
    "email": filter_users_by_email
}


if __name__ == "__main__":
    filter_option = (input(f"What would you like to filter by? (Currently, {get_options()} is supported): ").strip()
                     .lower())

    if filter_option in commands.keys():
        commands[filter_option]()
    else:
        print("Filtering by that option is not yet supported.")
