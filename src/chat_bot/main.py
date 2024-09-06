import sys
from datetime import datetime, timedelta, timezone


def __add_option_res() -> str:
    number_1: float = float(input("Please, enter the first number: "))
    number_2: float = float(input("Please, enter the second number: "))
    return f"Your solution: {number_1} + {number_2} = {number_1 + number_2}"


def get_response(text: str) -> str:
    current_time: datetime = datetime.now(timezone(-timedelta(hours=3)))
    options: dict = {
        text if text in ["hello", "hi", "hey"] else None: "Hey there!",
        text if "how are you" in text else None: "I'm good thanks!",
        text if "your name" in text else None: "My name is Bot :)",
        text if "time" in text else None: f"The time is: {current_time:%H:%M}",
        (
            text if text in ["bye", "see you", "goodbye"] else None
        ): "It was nice talking to you! Bye!",
        text if "add" in text else None: __add_option_res,
    }
    return (
        options.get(text, f'Sorry, I do not understand: "{text}".')
        if "add" not in text
        else options.get(text, f'Sorry, I do not understand: "{text}".')()
    )


user_name: str = input(
    "Bot: Hi! My name is Bot and I wanna know what's your name?\n",
).capitalize()
print(f"Bot: Nice to meet you {user_name}")
while True:
    user_input: str = input(f"{user_name}: ").lower()

    if user_input == "exit":
        print("Bot: It was a pleasure talking to you!")
        sys.exit()
    bot_response: str = get_response(user_input)
    print(f"Bot: {bot_response}")
