import random
import time
import tkinter as tk
from tkinter import messagebox


class VocabularyQuiz:
    def __init__(self, root):

        # Create the main window
        self.root = root
        # Setting the title
        self.root.title("Vocabulary Quiz Game")
        # Set the window size
        self.root.geometry("800x600")  # You can adjust the size as needed


        self.word_dict = self.process_csv_and_return_dict()
        self.create_ui()

    def create_ui(self):
        # Create UI elements and layout
        self.title_label = tk.Label(self.root, text="Quiz Question", font=("Helvetica", 30))
        self.title_label.pack(pady=10)
        
        self.instructions_label = tk.Label(self.root, text="Instructions: Guess the meaning of each word", font=("Helvetica", 20))
        self.instructions_label.pack()
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 20))
        self.exit_button.pack(side="bottom", pady=10)
        
        self.select_game_mode_label = tk.Label(self.root, text="Select a game mode:", font=("Helvetica", 16))
        self.select_game_mode_label.pack(pady=10)
        
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
            self.label = tk.Label(self.root, text="Enter Lives:", font=("Helvetica", 20))
            self.label.pack(pady=50)
            
            self.lives_entry = tk.Entry(self.root, font=("Helvetica", 20))
            self.lives_entry.pack(pady=10)
            
            self.submit_button = tk.Button(self.root, text="Submit", font=("Helvetica", 15), command=self.get_lives)
            self.submit_button.pack()
        elif option == 2:
            self.label = tk.Label(self.root, text="Enter Time (in secs):", font=("Helvetica", 20))
            self.label.pack(pady=50)
            
            self.time_entry = tk.Entry(self.root, font=("Helvetica", 20))
            self.time_entry.pack(pady=10)
            
            self.submit_button = tk.Button(self.root, text="Submit", font=("Helvetica", 15), command=self.get_time)
            self.submit_button.pack()
        else:
            self.play_mode_without_lives()

    def clear_widgets_except_quit(self):
        # Clear all widgets except the Quit button
        for widget in self.root.winfo_children():
            if widget != self.exit_button:
                widget.destroy()


    def process_csv_and_return_dict(self):
        # Read and process the CSV file to create the word dictionary
        word_dict = {}
        # Your code for reading and processing the CSV file goes here
        return word_dict


    def get_lives(self):
        lives = int(self.lives_entry.get())
        self.clear_widgets_except_quit()
        self.play_mode_with_lives(lives)

    def get_time(self):
        time_limit = int(self.time_entry.get())
        self.clear_widgets_except_quit()
        self.play_mode_with_timer(time_limit)

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