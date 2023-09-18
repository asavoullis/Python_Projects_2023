import random
import time
import tkinter as tk
from tkinter import *
import copy


class VocabularyQuiz:
    def __init__(self, root):

        # Create the main window
        self.root = root
        # Setting the title
        self.root.title("Vocabulary Quiz Game")
        # Set the window size
        self.root.geometry("800x600")  # You can adjust the size as needed

        # Initialize with 3 lives
        self.lives = 3  

        # Initialize the time_limit variable to 120 seconds
        self.time_limit = 120

        self.word_dict = self.process_csv_and_return_dict()
        self.create_menu_ui()

    def create_game_ui(self):
        # game frame, its the frame inside the root frame
        self.game_frame = tk.Frame(root)
        # the root of lives_score_label is game_frame
        self.lives_score_label = tk.Label(self.game_frame, font=("Helvetica", 16))
        self.lives_score_label.pack(anchor="ne", padx=10, pady=10)  # Adjust padx and pady as needed

        # the root of time_score_label is game_frame
        self.time_score_label = tk.Label(self.game_frame, font=("Helvetica", 16))
        self.time_score_label.pack(anchor="ne", padx=10, pady=10)  # Adjust padx and pady as needed

        self.word_label = tk.Label(self.game_frame, font=("Helvetica", 25))
        self.word_label.pack(pady = 10)

        self.choice_label_list = []
        for i in range(0,4):
            self.choice_label_list.append(tk.Label(self.game_frame, font=("Helvetica", 25)))
            self.choice_label_list[i].pack(pady = 10)
        
        self.entry = tk.Entry(self.game_frame, width=20, font=("Helvetica", 20))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.game_frame, text="Submit", borderwidth=1, font=("Helvetica", 15), command=lambda: self.set_input(None))
        self.submit_button.pack()

        self.root.bind('<Return>', self.set_input)
        
        self.game_frame.pack(fill='both')

    def play_again(self, game_mode):
        self.game_lost_frame.pack_forget()
        self.game_lost_frame.destroy()
        if game_mode == 0:
            self.play_mode_with_lives()

    def to_menu(self):
        self.game_lost_frame.pack_forget()
        self.game_lost_frame.destroy()
        self.create_menu_ui()
    
    def create_game_lost_ui(self, score, game_mode):
        self.game_lost_frame = tk.Frame(self.root)
        self.game_lost_frame.pack()
        self.game_lost_label = tk.Label(self.game_lost_frame, text=f"Game over, score: {score}", font=("Helvetica", 25))
        self.game_lost_label.pack()
        self.game_lost_playAgain_button = tk.Button(self.game_lost_frame, text="Play Again", font=("Helvetica", 15), command=lambda : self.play_again(game_mode))
        self.game_lost_playAgain_button.pack()
        self.game_lost_menu_button = tk.Button(self.game_lost_frame, text="Go to Menu", font=("Helvetica", 15), command=lambda : self.to_menu())
        self.game_lost_menu_button.pack()

    def game_lost(self, score, game_mode):
        self.game_frame.pack_forget()
        self.game_frame.destroy()
        self.root.unbind('<Return>')
        self.create_game_lost_ui(score, game_mode)

    def play_mode_with_timer(self):
            wd_list = list(self.word_dict)
            score = 0
            # time remaining
            time_remaining = self.time_limit

            self.selection = tk.IntVar(master=self.root, value=None)
            self.create_game_ui()

            self.time_score_label["text"] = f"Lives:   {time_remaining}     Score:    {score}"

            while time_remaining > 0:
                word, definition, choice_list = self.get_question(wd_list)
                self.update_ui(choice_list, word)
                self.selection.set(None)
                root.wait_variable(self.selection)
                if self.check_answer(definition, choice_list) is True:
                    score += 1
                    self.time_score_label["text"] = f"Lives:   {time_remaining}     Score:    {score}"
                else:
                    lives -= 1
                    self.time_score_label["text"] = f"Lives:   {time_remaining}     Score:    {score}"
            
            self.game_lost(score, 0)
    

    def play_mode_with_lives(self):
        wd_list = list(self.word_dict)
        score = 0
        # lives remaining
        lives = self.lives
        self.selection = tk.IntVar(master=self.root, value=None)
        self.create_game_ui()

        self.lives_score_label["text"] = f"Lives:   {self.lives}     Score:    {score}"

        while lives > 0:
            word, definition, choice_list = self.get_question(wd_list)
            self.update_ui(choice_list, word)
            self.selection.set(None)
            root.wait_variable(self.selection)
            if self.check_answer(definition, choice_list) is True:
                score += 1
                self.lives_score_label["text"] = f"Lives:   {lives}     Score:    {score}"
            else:
                lives -= 1
                self.lives_score_label["text"] = f"Lives:   {lives}     Score:    {score}"
        
        self.game_lost(score, 0)

    def check_answer(self, definition, choice_list):
        # This function checks if the selected choice from the list of choices (choice_list)
        # matches the correct definition (definition).
        # It uses the currently selected index stored in self.selection to determine the chosen answer.
        return choice_list[self.selection.get() - 1] == definition
         
    def get_question(self, wd_list):
        # This function is used to generate a question and a list of answer choices.
        # It takes a list of word-definition pairs (wd_list) as input.

        # Initialize an empty list to store answer choices.
        choice_list = []
        
        # Generate four random word-definition pairs to use as answer choices.
        for _ in range(4):
            # Get a random word and its corresponding definition, removing it from the list.
            word, definition = self.get_def_and_pop(wd_list)
            # Add the definition to the list of answer choices.
            choice_list.append(definition)

        # Shuffle the list of answer choices to randomize their order.
        random.shuffle(choice_list)
        # Return the selected word as the question and the shuffled list of answer choices.
        return word, definition, choice_list

    def update_ui(self, choice_list, word):
        # the word that we are trying to find its meaning   
        self.word_label["text"] = word
        
        # gets the 4 different meanings 
        for idx, choice in enumerate(choice_list):
            self.choice_label_list[idx]["text"] = f"{idx+1}: {choice}"
        self.entry.delete(0, END)
        self.entry.focus()

    def set_input(self, event):
        self.submit_button.config(relief=tk.SUNKEN, borderwidth=1)
        self.root.after(100, lambda : self.submit_button.config(relief=tk.RAISED, borderwidth=1))
        try:
            input_value = int(self.entry.get())
            if input_value in (1, 2, 3, 4):
                self.selection.set(input_value)
                self.entry.delete(0, tk.END)  # Clear the input field
            else:
                # Handle the case where the input is not in (1, 2, 3, 4).
                self.entry.delete(0, tk.END)  # Clear the input field
        except ValueError:
            # Handle the case where the input is not a valid integer (e.g., letters or special characters).
            self.entry.delete(0, tk.END)  # Clear the input field


    def create_menu_ui(self):
        # Create UI elements and layout
        self.menu_frame = tk.Frame(root)
        self.menu_title_label = tk.Label(self.menu_frame, text="Quiz Question", font=("Helvetica", 30))
        self.menu_title_label.pack(pady=10)
        
        self.menu_instructions_label = tk.Label(self.menu_frame, text="Instructions: Guess the meaning of each word", font=("Helvetica", 20))
        self.menu_instructions_label.pack()
        
        self.menu_exit_button = tk.Button(self.menu_frame, text="Exit", command=self.root.quit, font=("Helvetica", 20))
        self.menu_exit_button.pack(side="bottom", pady=10)
        
        self.menu_select_game_mode_label = tk.Label(self.menu_frame, text="Select a game mode:", font=("Helvetica", 16))
        self.menu_select_game_mode_label.pack(pady=20)
        
        self.menu_message_button1 = tk.Button(self.menu_frame, text="Play with Lives", command=lambda: self.mode_selection(option=1), font=("Helvetica", 16))
        self.menu_message_button2 = tk.Button(self.menu_frame, text="Time Attack", command=lambda: self.mode_selection(option=2), font=("Helvetica", 16))
        self.menu_message_button3 = tk.Button(self.menu_frame, text="Warmup", command=lambda: self.mode_selection(option=3), font=("Helvetica", 16))
        
        self.menu_message_button1.pack(pady=30)
        self.menu_message_button2.pack(pady=30)
        self.menu_message_button3.pack(pady=30)

        self.menu_frame.pack()

    def mode_selection(self, option):
        # Handle mode selection based on the chosen option
        self.clear_widgets_except_quit()
        if option == 1:
            self.play_mode_with_lives()
        elif option == 2:
            self.play_mode_with_timer()
        else:
            self.play_mode_without_lives()
       

    def clear_widgets_except_quit(self):
        """ Clears all widgets except the Quit button """
        for widget in self.root.winfo_children():
            if widget != self.menu_exit_button:
                widget.destroy()


    def process_csv_and_return_dict(self):
        # Open the "Vocabulary_list.csv" file for reading
        fh = open("Vocabulary_list.csv", "r")
        # Read all lines from the file into a list
        wd_list = fh.readlines()
        # Close the file
        fh.close()
        # Convert the list into a set to remove duplicates
        wd_set = set(wd_list)
        # Create an empty dictionary to store word-definition pairs
        word_dict = dict()
        # Iterate through each line in the set
        for rawstring in wd_set:
            # Split each line into a word and its corresponding definition
            word, definition = rawstring.split(",", 1)
            # Add the word and definition to the dictionary after stripping extra characters
            word_dict[word] = definition.strip('" \n')  
        # Return the dictionary containing word-definition pairs
        return word_dict

    def get_def_and_pop(self, word_list):
        # Generate a random index within the range of the word list
        random_index = random.randrange(len(word_list))
        # Remove and retrieve a word from the list using the random index
        word = word_list.pop(random_index)
        # Get the corresponding definition from the word dictionary
        definition = self.word_dict.get(word)
        # Return the word and its definition
        return word, definition

    def start_game(self, mode):
        # Start the selected game mode
        if mode == "lives":
            self.play_mode_with_lives()
        elif mode == "timer":
            self.play_mode_with_timer()
        elif mode == "warmup":
            self.play_mode_without_lives()


if __name__ == "__main__":
    root = tk.Tk()
    game = VocabularyQuiz(root)
    root.mainloop()