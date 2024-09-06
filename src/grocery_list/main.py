import sys


def default_exception_msg(e: Exception) -> None:
    print(
        f"Unexpected error {e};"
        + f"\nType: {type(e)};"
        + f"\nRepresentation: {e!r}.",
    )


def welcome_message() -> None:
    print("Welcome to Groceries!")
    print("Enter: ")
    print("-" * 20)
    print("1 - To add an item")
    print("2 - To remove an item")
    print("3 - To list all items")
    print("4 - To edit a list item")
    print("0 - To exit the program")
    print("-" * 20)


def verify_input_item(item: str) -> bool:
    if item:
        return True
    return False


def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f'"{item}" has been added!')


def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'"{item}" has been removed!')
    except ValueError:
        print(f'NO "{item}" found in: {groceries}')
    except Exception as e:
        default_exception_msg(e)


def item_exists(item: str, groceries: list[str]) -> bool:
    if item in groceries:
        return True
    return False


def edit_item(item: str, new_item: str, groceries: list[str]) -> None:
    groceries[groceries.index(item)] = new_item
    print(f'"{item}" was changed by "{new_item}"')


def display(groceries: list[str]) -> None:
    print("___LIST___")
    for i, item in enumerate(groceries, 1):
        print(f"{i}: {item.capitalize()}")

    print("_" * 10)


def is_an_option(text: str) -> bool:
    return text in ["1", "2", "3", "4", "0"]


def main() -> None:
    groceries: list[str] = []
    welcome_message()
    while True:
        user_input: str = input("Chose: ").lower()

        if not is_an_option(user_input):
            print("Please pick a valid option...")
            continue

        if user_input == "1":
            new_item: str = input("What item would you like to add? >> ").lower()
            if not verify_input_item(new_item):
                print("Please, enter a valid item...")
                continue
            add_item(new_item, groceries)
        elif user_input == "2":
            item_to_removed: str = input(
                "What item would you like to remove? >> ",
            ).lower()
            remove_item(item_to_removed, groceries)
        elif user_input == "3":
            display(groceries)
        elif user_input == "4":
            if len(groceries) == 0:
                print("No grocery registered...")
                continue
            existed_item: str = input("What item would you like to change? >> ").lower()
            if not item_exists(existed_item, groceries):
                print(f'The "{existed_item}" doesn\'t exist...')
                continue
            item: str = input("What is the new item name? >> ").lower()
            edit_item(existed_item, item, groceries)
        elif user_input == "0":
            print("Exiting program...")
            sys.exit(0)


if __name__ == "__main__":
    main()
