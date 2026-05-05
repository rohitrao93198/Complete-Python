import random
import tkinter as tk
from tkinter import messagebox

# Scores
humscore = 0
comscore = 0

choices = {1: "Stone", 2: "Paper", 3: "Scissor"}


# Game logic function
def play(user):
    global humscore, comscore

    com = random.randint(1, 3)

    user_choice.set(f"You chose: {choices[user]}")
    com_choice.set(f"Computer chose: {choices[com]}")

    if user == com:
        result.set("🤝 It's a Tie!")

    elif (
        (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2)
    ):
        humscore += 1
        result.set("✅ You won this round!")

    else:
        comscore += 1
        result.set("💻 Computer won this round!")

    score.set(f"Score ➜ You: {humscore} | Computer: {comscore}")

    # Winning condition
    if humscore == 5:
        messagebox.showinfo("Game Over", "🏆 You won the game!")
        reset_game()

    elif comscore == 5:
        messagebox.showinfo("Game Over", "💻 Computer won the game!")
        reset_game()


def reset_game():
    global humscore, comscore
    humscore = 0
    comscore = 0
    score.set("Score ➜ You: 0 | Computer: 0")
    result.set("")
    user_choice.set("")
    com_choice.set("")


# UI Setup
root = tk.Tk()
root.title("Stone Paper Scissor Game 🎮")
root.geometry("400x400")

# Variables for UI
score = tk.StringVar(value="Score ➜ You: 0 | Computer: 0")
result = tk.StringVar()
user_choice = tk.StringVar()
com_choice = tk.StringVar()

# Title
tk.Label(root, text="Stone Paper Scissor", font=("Arial", 16, "bold")).pack(pady=10)

# Score
tk.Label(root, textvariable=score, font=("Arial", 12)).pack()

# Choices display
tk.Label(root, textvariable=user_choice).pack()
tk.Label(root, textvariable=com_choice).pack()

# Result
tk.Label(root, textvariable=result, font=("Arial", 12, "bold")).pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="🪨 Stone", width=10, command=lambda: play(1)).grid(
    row=0, column=0, padx=5
)
tk.Button(frame, text="📄 Paper", width=10, command=lambda: play(2)).grid(
    row=0, column=1, padx=5
)
tk.Button(frame, text="✂️ Scissor", width=10, command=lambda: play(3)).grid(
    row=0, column=2, padx=5
)

# Reset button
tk.Button(root, text="🔄 Reset Game", command=reset_game).pack(pady=10)

# Run app
root.mainloop()
