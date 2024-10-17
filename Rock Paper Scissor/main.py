import tkinter as tk
import random

def play(choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    if choice == computer_choice:
        result.set(f"Both chose {choice}. It's a tie!")
    elif (choice == 'Rock' and computer_choice == 'Scissors') or \
         (choice == 'Paper' and computer_choice == 'Rock') or \
         (choice == 'Scissors' and computer_choice == 'Paper'):
        result.set(f"You chose {choice}. Computer chose {computer_choice}. You win!")
    else:
        result.set(f"You chose {choice}. Computer chose {computer_choice}. You lose.TRY AGAIN....")
        


root = tk.Tk()
root.title("Rock Paper Scissors")


result = tk.StringVar()


title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 16))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play('Rock'),bg='light green')
rock_button.pack(side=tk.LEFT, padx=15)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play('Paper'),bg='orange')
paper_button.pack(side=tk.LEFT, padx=15)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play('Scissors'),bg='blue')
scissors_button.pack(side=tk.RIGHT, padx=15)

result_label = tk.Label(root, textvariable=result, font=("Helvetica", 14))
result_label.pack(pady=20)


root.mainloop()
