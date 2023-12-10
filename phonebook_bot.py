def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Provide sufficient arguments."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if contacts.get(name) is None:
      contacts[name] = phone
      return "Contact added."
    else:
      return change_contact(args, contacts)

@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name) is not None:
        contacts.update({name: phone})
        return "Contact changed."
    else:
        return add_contact(args, contacts)

@input_error
def contact(name, contacts):
    return contacts.get(name)

def get_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(get_contacts(contacts))
        elif command == "phone":
            print(contact(args[0], contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()