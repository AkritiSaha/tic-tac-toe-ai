import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

board = [" " for _ in range(9)]
buttons = []


# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


# Check draw
def is_draw():
    return " " not in board


# Minimax
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


# AI move
def ai_move():
    best_score = -float("inf")
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    buttons[move].config(text="O", state="disabled")


# Handle button click
def on_click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You Win!")
            reset_game()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "Draw!")
            reset_game()
            return

        ai_move()

        if check_winner("O"):
            messagebox.showinfo("Game Over", "AI Wins!")
            reset_game()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "Draw!")
            reset_game()


# Reset game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text="", state="normal")


# Create buttons
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Restart button
reset_btn = tk.Button(root, text="Restart", font=("Arial", 14), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Run app
root.mainloop()