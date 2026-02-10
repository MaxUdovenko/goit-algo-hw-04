def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "ERROR: It is possibly that you have input wrong arguments: name or phone"


def show_phone(args, contacts):
    try:
        return contacts.get(args[0], "No such name in phonebook")
    except IndexError:
        return "ERROR: The `name` argument is empty"


def show_all(contacts):
    for k, v in contacts.items():
        print(f"name: {k}, phone: {v}")


def change_contact(args, contacts):
    try:
        name, new_phone = args
        contacts[name] = new_phone
        return "Contact changed."
    except ValueError:
        return "ERROR: It is possibly that you have input wrong arguments: name or phone"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                return False
            case "hello":
                print("How can I help you?")
            case "add":
                # "add [ім'я] [номер телефону]"
                print(add_contact(args, contacts))
            case "change":
                # "change [ім'я] [новий номер телефону]"
                change_contact(args,contacts)
            case "phone":
                # "phone [ім'я]"
                print(show_phone(args, contacts))
            case "all":
                show_all(contacts)
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()