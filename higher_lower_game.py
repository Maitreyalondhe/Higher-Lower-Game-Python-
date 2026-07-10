
import art
import game_data
import random

score = 0
game_over = False

a = random.choice(game_data.data)
b = random.choice(game_data.data)

while a == b:
    b = random.choice(game_data.data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def check_answer(user_choice, a_followers, b_followers):
    if a_followers > b_followers and user_choice == "a":
        return True
    elif b_followers > a_followers and user_choice == "b":
        return True
    else:
        return False


while not game_over:
    print("\n" * 50)
    print(art.logo)
    print(f"Compare A: {format_data(a)}")
    print(art.vs)
    print(f"Compare B: {format_data(b)}")

    a_followers = a["follower_count"]
    b_followers = b["follower_count"]


    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    while choice != "a" and choice != "b":
        print("Please enter a valid Option.")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_answer(choice, a_followers, b_followers):
        score += 1
        print(f"Current score: {score}")
        if b_followers > a_followers:
            a = b
        b = random.choice(game_data.data)
        while a == b:
            b = random.choice(game_data.data)

    else:
        print(f"Game over! Final score: {score}")
        game_over = True







