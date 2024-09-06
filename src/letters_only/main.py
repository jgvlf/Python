import string


def is_only_letters(text: str) -> None:
    alphabet: str = (
        string.ascii_letters + "ãÃõÕâÂêÊîÎôÔûÛáÁéÉíÍóÓúÚàÀèÈìÌòÒùÙ" + "çÇ" + " "
    )
    for char in text:
        if char not in alphabet:
            raise ValueError("The text isn't contain only letters...")
    print(f'"{text}" is only letters, good job!')


def main() -> None:
    while True:
        try:
            user_input: str = input("Check the text: ")
            is_only_letters(user_input)
        except ValueError:
            print("Please only enter a Portuguese letters...")
        except Exception as e:
            print(
                f"Found a unexpected error: \nRepresentation: {e!r}; \nType: {type(e)}; \nValue: {e}",
            )


if __name__ == "__main__":
    main()
