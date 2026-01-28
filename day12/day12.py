from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks the user's guess against the answer and returns remaining turns."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1

    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

turns = set_difficulty()

guess = 0
while guess != answer and turns > 0:
    print(f"You have {turns} attempts remaining to guess

