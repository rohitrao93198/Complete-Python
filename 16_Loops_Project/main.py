# 1st game - Number Predictor

# import random

# num = random.randint(1, 100)

# tries = 0
# while True:
#     guessed = int(input("guess the number between 1 - 100 : "))
#     tries = tries + 1
#     if guessed == num:
#         print(f"Congrats you find your number in {tries} tries")
#         break
#     elif guessed > num:
#         print("sorry you need to go lower")
#     elif guessed < num:
#         print("sorry you have to go little bit upper")


# 2nd game - Stone, paper and scissor
# import random

# comscore = 0
# humscore = 0
# while True:
#     print(f"current scores You - {humscore} computer - {comscore}/n")
#     user = int(input("1 for stone, 2 for paper, 3 for scissor choose :- "))
#     com = random.randint(1, 3)

#     if user == 1 and com == 3:
#         humscore = humscore + 1
#         print("user won the round \n")
#     elif user == 2 and com == 1:
#         humscore = humscore + 1
#         print("user won this round \n")
#     elif user == 3 and com == 2:
#         humscore = humscore + 1
#         print("user won this round \n")
#     elif user == com:
#         print("it was a tie")
#     else:
#         comscore = comscore + 1
#         print("computer won this round")

#     if comscore == 5:
#         print("Computer won this game")
#         break
#     elif humscore == 5:
#         print("Congrats You won this game")
#         break
#     elif comscore == humscore:
#         print("This was Tie")
#         break


import random

comscore = 0
humscore = 0

choices = {1: "Stone", 2: "Paper", 3: "Scissor"}

print("🎮 Welcome to Stone Paper Scissor Game!")

while True:
    print("\n----------------------------------")
    print(f"Score ➜ You: {humscore} | Computer: {comscore}")
    print("----------------------------------")

    user = int(input("1: Stone | 2: Paper | 3: Scissor | 0: Exit ➜ "))

    if user == 0:
        print("Game exited 👋")
        break

    if user not in [1, 2, 3]:
        print("❌ Invalid choice, try again!")
        continue

    com = random.randint(1, 3)

    print(f"\nYou chose: {choices[user]}")
    print(f"Computer chose: {choices[com]}\n")

    # Game logic
    if user == com:
        print("🤝 It's a Tie!")

    elif (
        (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2)
    ):
        humscore += 1
        print("✅ You won this round!")

    else:
        comscore += 1
        print("💻 Computer won this round!")

    # Winning condition
    if humscore == 5:
        print("\n🏆 CONGRATULATIONS! You won the game!")
        break

    elif comscore == 5:
        print("\n💻 Computer won the game! Better luck next time.")
        break
