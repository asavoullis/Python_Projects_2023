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
        self.create_ui()

    def create_game_ui(self):
        self.lives_score_label = tk.Label(root, font=("Helvetica", 16))
        self.lives_score_label.pack(anchor="ne", padx=10, pady=10)  # Adjust padx and pady as needed

        self.word_label = tk.Label(root, font=("Helvetica", 25))
        self.word_label.pack(pady = 10)

        self.choice_label_list = []
        for i in range(0,4):
            self.choice_label_list.append(tk.Label(root, font=("Helvetica", 25)))
            self.choice_label_list[i].pack(pady = 10)
        
        self.entry = tk.Entry(root, width=20, font=("Helvetica", 20))
        self.entry.pack(pady=5)

        submit_button = tk.Button(root, text="Submit",font=("Helvetica", 15), command=lambda: self.set_input(None))
        submit_button.pack()

        self.root.bind('<Return>', self.set_input)

    def play_mode_with_lives(self):
        wd_list = list(self.word_dict)
        score = 0
        # lives remaining
        lives = self.lives
        self.selection = tk.IntVar(master=self.root, value=None)
        self.create_game_ui()

        self.lives_score_label["text"] = f"Lives:   {self.lives}     Score:    {score}"
        #lives_score_label.pack(anchor="ne", padx=10, pady=10)  # Adjust padx and pady as needed

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
        
        print("no more lives remaining")

    def check_answer(self, definition, choice_list):
        return choice_list[self.selection.get() - 1] == definition
         
    def get_question(self, wd_list):
        choice_list = []
        for _ in range(4):
            word, definition = self.get_def_and_pop(wd_list)
            choice_list.append(definition)
        random.shuffle(choice_list)
        return word, definition, choice_list

    def update_ui(self, choice_list, word):
        
        # the word that we are trying to find its meaning   
        self.word_label["text"] = word
        
        # gets the 4 different meanings 
        for idx, choice in enumerate(choice_list):
            self.choice_label_list[idx]["text"] = f"{idx+1}: {choice}"
        self.entry.delete(0, END)
        self.entry.focus()

    def set_input(self, event=None):
        self.selection.set(self.entry.get())


    def create_ui(self):
        # Create UI elements and layout
        self.title_label = tk.Label(self.root, text="Quiz Question", font=("Helvetica", 30))
        self.title_label.pack(pady=10)
        
        self.instructions_label = tk.Label(self.root, text="Instructions: Guess the meaning of each word", font=("Helvetica", 20))
        self.instructions_label.pack()
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 20))
        self.exit_button.pack(side="bottom", pady=10)
        
        self.select_game_mode_label = tk.Label(self.root, text="Select a game mode:", font=("Helvetica", 16))
        self.select_game_mode_label.pack(pady=20)
        
        self.message_button1 = tk.Button(self.root, text="Play with Lives", command=lambda: self.mode_selection(option=1), font=("Helvetica", 16))
        self.message_button2 = tk.Button(self.root, text="Time Attack", command=lambda: self.mode_selection(option=2), font=("Helvetica", 16))
        self.message_button3 = tk.Button(self.root, text="Warmup", command=lambda: self.mode_selection(option=3), font=("Helvetica", 16))
        
        self.message_button1.pack(pady=30)
        self.message_button2.pack(pady=30)
        self.message_button3.pack(pady=30)

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
            if widget != self.exit_button:
                widget.destroy()


    def process_csv_and_return_dict(self): 
        fh = open("Vocabulary_list.csv", "r")
        wd_list = fh.readlines()
        fh.close()

        wd_set = set(wd_list)

        word_dict = dict()
        for rawstring in wd_set:
            word, definition = rawstring.split(",", 1)
            word_dict[word] = definition.strip('" \n')  
        return word_dict

    def get_def_and_pop(self, word_list):
        random_index = random.randrange(len(word_list))
        word = word_list.pop(random_index)
        definition = self.word_dict.get(word)
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