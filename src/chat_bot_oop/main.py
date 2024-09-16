from secrets import choice
from datetime import datetime

from chat_bot_oop.country import Country
from zoneinfo import ZoneInfo

class ChatBot:
    def __init__(self, name: str, age: int, locally: Country) -> None:
        self.name = name
        self.age = age
        self.__tz = locally.value

    def get_description(self) -> str:
        return f"{self.name} is a bot who is {self.age} years old."

    def __get_response(self, text: str) -> str:
        lowered: str = text.lower()
        match lowered:
            case lowered if "hello" in lowered:
                return f"{self.name}: Hey there!"
            case lowered if "bye" in lowered:
                return f"{self.name}: See you!"
            case lowered if "how old are you" in lowered:
                return f"{self.name}: I am {self.age} years old!"
            case lowered if "what time is it" in lowered:
                now: datetime = datetime.now(tz=ZoneInfo(self.__tz))
                return f"{self.name}: The current time is {now:%H:%M:%S}"
            case lowered if "how are you" in lowered:
                return f"{self.name}: Great, thanks!"
            case _:
                random_responses: list[str] = ["I don't understand...",
                                               "Would you mind rephrasing that.",
                                               "What?",
                                               "Ah, what?"]
                return f"{self.name}: {choice(random_responses)}"

    def run(self) -> None:
        while True:
            user_input: str = input("You: ")
            if user_input == "exit":
                print(f"Thank you for chatting with {self.name}!")
                break

            response: str = self.__get_response(user_input)
            print(response)


def main() -> None:
    mario: ChatBot = ChatBot("Mario", 27, Country.USA_LA)
    silvio: ChatBot = ChatBot("Silvio", 57, Country.BR)

    print(mario.get_description())
    mario.run()

    print(silvio.get_description())
    silvio.run()


if __name__ == "__main__":
    main()
