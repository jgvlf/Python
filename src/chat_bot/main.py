import sys
from datetime import datetime, timedelta, timezone


def get_response(text: str) -> str:
    if text in ["hello", "hi", "hey"]:
        return "Hey there!"
    if "how are you" in text:
        return "I'm good thanks!"
    if "your name" in text:
        return "My name is Bot :)"
    if "time" in text:
        current_time: datetime = datetime.now(timezone(-timedelta(hours=3)))
        return f"The time is: {current_time:%H:%M}"
    if text in ["bye", "see you", "goodbye"]:
        return "It was nice talking to you! Bye!"
    if "add" in text:
        number_1: float = float(input("Please, enter the first number: "))
        number_2: float = float(input("Please, enter the second number: "))
        return f"Your solution: {number_1} + {number_2} = {number_1 + number_2}"
    return f'Sorry, I do not understand: "{text}".'


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
