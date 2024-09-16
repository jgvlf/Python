name: str = input("Enter a name: ")
noun_a: str = input("Enter a noun: ")
verb_a: str = input("Enter a verb: ")
noun_b: str = input("Enter a noun: ")
verb_b: str = input("Enter a verb (past tense): ")
number_a: str = input("Enter a number: ")
number_b: str = input("Enter a another number: ")


story: str = f"""
-------------------------------------------------------------------------------
A guy called {name} has a beautiful {noun_a} and always {verb_a}
before the work.

In a Olympics game, this fella {verb_b} and receive {noun_b} as a prize.

Your age is {int(number_a) + int(number_b)} and is retired of his adventures...

But your legacy won't be forgotten...
-------------------------------------------------------------------------------
"""

print(story)
