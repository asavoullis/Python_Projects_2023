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
    # display lives
    score = 0
    lives_score_label = tk.Label(root, text=f"Lives : {lives},     Score :  {score}" , font=("Helvetica", 16))
    lives_score_label.pack(anchor="ne", padx=10, pady=10)  # Adjust padx and pady as needed

    while lives > 0:
        wd_list = list(word_dict)
        choice_list = []
        for x in range(4):
            word, definition = get_def_and_pop(wd_list, word_dict)
            choice_list.append(definition)
        random.shuffle(choice_list)
        
        # the word that we are trying to find its meaning
        word = tk.Label(root, text=word, font=("Helvetica", 25))
        word.pack(pady = 10)

        # gets the 4 different meanings 
        for idx, choice in enumerate(choice_list):
            choice_label = tk.Label(root, text=f"{idx+1}: {choice}", font=("Helvetica", 25))
            choice_label.pack(pady = 10)

        entry = tk.Entry(root, width=20, font=("Helvetica", 20))
        entry.pack(pady=5)
        submit_button = tk.Button(root, text="Submit",font=("Helvetica", 15), command=lambda: get_lives(word_dict, entry))
        submit_button.pack()

        while True:
            try:
                if 1 <= entry.get() <= 4:
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

# Function to show message boxes
def show_message_box(box_number):
    if box_number == 1:
        messagebox.showinfo("Info", "This is an informational message.")
    elif box_number == 2:
        messagebox.showwarning("Warning", "This is a warning message.")
    elif box_number == 3:
        messagebox.showerror("Error", "This is an error message.")

def process_csv_and_return_dict(): 
    fh = open("Vocabulary_list.csv", "r")
    wd_list = fh.readlines()
    fh.close()

    wd_set = set(wd_list)

    word_dict = dict()
    for rawstring in wd_set:
        word, definition = get_word_and_definition(rawstring)
        word_dict[word] = definition
    return word_dict

def clear_widgets_except_quit():
    # Destroy all widgets except the Quit button
    for widget in root.winfo_children():
        if widget != exit_button:
            widget.destroy()

def mode_selection(option):
    # clearing the screen to make new widgets
    clear_widgets_except_quit()

    # creating the word dict
    word_dict = process_csv_and_return_dict()

    if option == 1:
        # Create an input field for the number of lives
        label = tk.Label(root, text="Enter Lives:", font=("Helvetica", 20))
        label.pack(pady = 50)
        
        lives_entry = tk.Entry(root, font=("Helvetica", 20))
        lives_entry.pack(pady = 10)
        
        submit_button = tk.Button(root, text="Submit",font=("Helvetica", 15), command=lambda: get_lives(word_dict, lives_entry))
        submit_button.pack()
    elif option == 2:
        # Create an input field for the time
        label = tk.Label(root, text="Enter Time (in secs):", font=("Helvetica", 20))
        label.pack(pady = 50)
        
        time_entry = tk.Entry(root, font=("Helvetica", 20))
        time_entry.pack(pady = 10)
        
        submit_button = tk.Button(root, text="Submit",font=("Helvetica", 15), command=lambda: get_time(word_dict, time_entry))
        submit_button.pack()
    else:
        play_mode_without_lives(word_dict)

def get_lives(word_dict, lives_entry):
    lives = int(lives_entry.get())
    clear_widgets_except_quit()
    play_mode_with_lives(word_dict, lives)

def get_time(word_dict, time_entry):
    time = int(time_entry.get())
    clear_widgets_except_quit()
    play_mode_with_timer(word_dict, time)


if __name__ == "__main__":
    

    # Create the main window
    root = tk.Tk()
    root.title("Vocabulary Quiz Game")

    # Set the window size
    root.geometry("800x600")  # You can adjust the size as needed

    # Create a label with a larger font
    Title_Label = tk.Label(root, text="Quiz Question", font=("Helvetica", 30))
    Title_Label.pack(pady = 10)
    Instructions_Label = tk.Label(root, text="Instructions: Guess the meaning of each word", font=("Helvetica", 20))
    Instructions_Label.pack()

    # Quit button
    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 20))
    exit_button.pack(side="bottom", pady=10)  # Adjust the value of pady as needed

    Select_Game_Mode_Label = tk.Label(root, text="Select a game mode:", font=("Helvetica", 16))
    Select_Game_Mode_Label.pack(pady = 10)


    # Three buttons to show message boxes
    message_button1 = tk.Button(root, text="Play with Lives", command=lambda: mode_selection(option=1), font=("Helvetica", 16))
    message_button2 = tk.Button(root, text="Time Attack", command=lambda: mode_selection(option=2), font=("Helvetica", 16))
    message_button3 = tk.Button(root, text="Warmup", command=lambda: mode_selection(option=3), font=("Helvetica", 16))
 
    message_button1.pack(pady = 30)
    message_button2.pack(pady = 30)
    message_button3.pack(pady = 30)

    

    # Start the Tkinter main loop
    root.mainloop()
