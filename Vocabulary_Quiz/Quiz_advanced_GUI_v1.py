import random
import time
import tkinter as tk
from tkinter import messagebox

def get_word_and_definition(rawstring: str):
    word, definition = rawstring.split(",", 1)
    return word, definition.strip('" \n')  # Updated to remove " and \n

def get_def_and_pop(word_list, word_dict):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition

def play_mode_with_lives(word_dict, lives):
    score = 0
    while lives > 0:
        wd_list = list(word_dict)
        choice_list = []
        for x in range(4):
            word, definition = get_def_and_pop(wd_list, word_dict)
            choice_list.append(definition)
        random.shuffle(choice_list)

        print(word)
        print("--------------------------------")
        for idx, choice in enumerate(choice_list):
            print(idx+1, choice)

        while True:
            try:
                choice = int(input("Enter 1, 2, 3, or 4; 0 to exit: "))
                if choice == 0:
                    break
                elif 1 <= choice <= 4:
                    break
                else:
                    print("\n")
                    print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")
            except ValueError:
                print("\n")
                print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")

        if choice == 0:
            break
        elif choice_list[choice - 1] == definition:
            score += 1
            print("\nCorrect!, You have", lives, "lives remaining.  Your score is:", score, "\n")
        else:
            lives -= 1
            print("\nIncorrect! You have", lives, "lives remaining.  Your score is:", score, "\n")

    print("Quiz Ended")
    print("Your Final Score:", score)

def play_mode_with_timer(word_dict, total_time_limit):
    score = 0
    start_time = time.time()
    word_number = 0

    while True:
        # Check if time limit has exceeded
        elapsed_time = time.time() - start_time
        time_remaining = int(total_time_limit - elapsed_time)
        if elapsed_time >= total_time_limit:
            print("Time's up! Quiz ended.")
            time_remaining = 0
            break

        wd_list = list(word_dict)
        choice_list = []
        for x in range(4):
            word, definition = get_def_and_pop(wd_list, word_dict)
            choice_list.append(definition)
        random.shuffle(choice_list)

        print(word)
        word_number += 1
        print("--------------------------------")
        for idx, choice in enumerate(choice_list):
            print(idx+1, choice)

        while True:
            try:
                choice = int(input("Enter 1, 2, 3, or 4; 0 to exit: "))
                if choice == 0:
                    break
                elif 1 <= choice <= 4:
                    break
                else:
                    print("\n")
                    print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")
            except ValueError:
                print("\n")
                print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")

        if choice == 0:
            break
        elif choice_list[choice - 1] == definition:
            score += 1
            print("\nCorrect!")
            print("(Score:", score, "    Time Remaining:", time_remaining, "\n")
        else:
            print("\nIncorrect!")
            print("Score:", score,  "    Time Remaining:", time_remaining, "\n")

    print("Quiz Ended")
    print("Your Score:", score)

def play_mode_without_lives(word_dict):
    score = 0
    word_number = 0
    while True:
        wd_list = list(word_dict)
        choice_list = []
        for x in range(4):
            word, definition = get_def_and_pop(wd_list, word_dict)
            choice_list.append(definition)
        random.shuffle(choice_list)

        print(word)
        word_number += 1
        print("--------------------------------")
        for idx, choice in enumerate(choice_list):
            print(idx+1, choice)

        while True:
            try:
                choice = int(input("Enter 1, 2, 3, or 4; 0 to exit: "))
                if choice == 0:
                    break
                elif 1 <= choice <= 4:
                    break
                else:
                    print("\n")
                    print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")
            except ValueError:
                print("\n")
                print("Invalid input. Please enter a valid choice (0, 1, 2, 3, or 4).")

        if choice == 0:
            break
        elif choice_list[choice - 1] == definition:
            score += 1
            print("\nCorrect!")
            print("(Score:", score, "    Word Number:", word_number, "\n")
        else:
            print("\nIncorrect!")
            print("Score:", score,  "    Word Number:", word_number, "\n")

    print("Quiz Ended")
    print("Your Score:", score)

# Load vocabulary data from a file
with open("Vocabulary_list.csv", "r") as fh:
    wd_list = fh.readlines()

wd_set = set(wd_list)

word_dict = dict()
for rawstring in wd_set:
    word, definition = get_word_and_definition(rawstring)
    word_dict[word] = definition

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Vocabulary Quiz Game")

    # Create labels and entry widgets for configuration
    lives_label = tk.Label(root, text="Enter the number of lives:")
    lives_label.pack()
    lives_entry = tk.Entry(root)
    lives_entry.pack()

    timer_label = tk.Label(root, text="Enter the time limit per question (in seconds):")
    timer_label.pack()
    timer_entry = tk.Entry(root)
    timer_entry.pack()

    # Create buttons to start different quiz modes
    with_lives_button = tk.Button(root, text="Start Quiz with Lives", command=lambda: play_mode_with_lives(word_dict, int(lives_entry.get())))
    with_lives_button.pack()

    without_lives_button = tk.Button(root, text="Start Quiz without Lives", command=lambda: play_mode_without_lives(word_dict))
    without_lives_button.pack()

    with_timer_button = tk.Button(root, text="Start Quiz with Timer", command=lambda: play_mode_with_timer(word_dict, float(timer_entry.get())))
    with_timer_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack()

    # Start the GUI main loop
    root.mainloop()
