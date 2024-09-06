import random
import sys

# STEP 1: STARTING INFORMATION
print("Welcome to RPS!")
moves: dict = {"rock": "🪨", "paper": "📜", "scissors": "✂️"}
score: dict = {"You": 0, "AI": 0}
valid_moves: list[str] = list(moves.keys())

# STEP 2: INFINITE LOOP
while True:
    user_move: str = input("Rock, Paper, or Scissors? >> ").lower()

    if user_move == "exit":
        print("Thanks for playing!")
        sys.exit()

    if user_move == "score":
        print("------")
        print(f"You: {score['You']}")
        print(f"AI: {score['AI']}")
        print("------")
        if score["You"] == score["AI"]:
            print("It's a tie. Let's move on! You can do it!!")
        elif score["You"] > score["AI"]:
            print("You Winning!!! Continue as you be!!!")
        else:
            print(
                "You Lossing... It's time to a game change, let's turn the game aroud!",
            )
        continue

    if user_move not in valid_moves:
        print("Invalid move...")
        continue

    # AI decides
    ai_move: str = random.choice(valid_moves)

    print("------")
    print(f"You: {moves[user_move]}")
    print(f"AI: {moves[ai_move]}")
    print("------")

    # Check moves
    if user_move == ai_move:
        print("It is a tie!")
    elif user_move == "rock" and ai_move == "scissors" or user_move == "scissors" and ai_move == "paper" or user_move == "paper" and ai_move == "rock":
        print("You win!")
        score["You"] += 1
    else:
        print("AI wins...")
        score["AI"] += 1
