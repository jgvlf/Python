import sys
from datetime import datetime, timedelta, timezone


def __add_option_res() -> str:
    number_1: float = float(input("Please, enter the first number: "))
    number_2: float = float(input("Please, enter the second number: "))
    return f"Your solution: {number_1} + {number_2} = {number_1 + number_2}"


def get_response(text: str) -> str:  # noqa: PLR0911
    match text:
        case "hello" | "hi" | "hey":
            return "Hey there!"
        case t if "how are you" in t:
            return "I'm good thanks!"
        case t if "your name" in t:
            return "My name is Bot :)"
        case t if "time" in t:
            current_time: datetime = datetime.now(timezone(-timedelta(hours=3)))
            return f"The time is: {current_time:%H:%M}"
        case "bye" | "see you" | "goodbye":
            return "It was nice talking to you! Bye!"
        case t if "add" in t:
            return __add_option_res()
        case t:
            return f'Sorry, I do not understand: "{t}".'


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
