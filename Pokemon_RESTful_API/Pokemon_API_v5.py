import requests
import random
import tkinter as tk
from tkinter import messagebox

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.stats = {}
    
    def fetch_data(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            self.stats["Name"] = data["name"]
            for stat in data["stats"]:
                self.stats[stat["stat"]["name"]] = stat["base_stat"]
        else:
            messagebox.showerror("Error", f"Failed to fetch data for {self.name}")
    
    def display_stats(self):
        messagebox.showinfo(
            "Pokemon Stats",
            f"Pokemon: {self.stats['Name']}\nStats:\n" +
            "\n".join([f"{stat_name}: {stat_value}" for stat_name, stat_value in self.stats.items() if stat_name != "Name"])
        )

def fetch_random_pokemon():
    random_pokemon_id = random.randint(1, 898)
    pokemon_name = str(random_pokemon_id)
    pokemon = Pokemon(pokemon_name)
    pokemon.fetch_data()
    pokemon.display_stats()

def search_by_pokedex_number(pokedex_number):
    pokemon = Pokemon(pokedex_number)
    pokemon.fetch_data()
    pokemon.display_stats()

def display_generation_pokemon(generation):
    url = f"https://pokeapi.co/api/v2/generation/{generation}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Create a list of Pokemon names with their Pokedex numbers
        pokemon_list = [f"{pokemon['url'].split('/')[-2]}: {pokemon['name']}" for pokemon in data["pokemon_species"]]
        
        # Display the Pokemon names in multiple columns
        columns = 3  # Adjust the number of columns as needed
        rows = (len(pokemon_list) + columns - 1) // columns
        result = "\n".join([f"{pokemon_list[i]:<30}" for i in range(0, len(pokemon_list), rows)])
        
        messagebox.showinfo(f"Pokemon in Generation {generation}", result)
    else:
        messagebox.showerror("Error", f"Failed to fetch Generation {generation} data")

def on_option_selected(option):
    if option == 1:
        pokemon_name = entry_pokemon_name.get().lower()
        pokemon = Pokemon(pokemon_name)
        pokemon.fetch_data()
        pokemon.display_stats()
    elif option == 2:
        generation_option = int(entry_generation.get())
        display_generation_pokemon(generation_option)
    elif option == 3:
        pokedex_number = entry_pokedex_number.get()
        search_by_pokedex_number(pokedex_number)
    elif option == 4:
        fetch_random_pokemon()
    elif option == 5:
        window.quit()

# Create the main GUI window
window = tk.Tk()
window.title("Pokemon Data Program")

# Customize the font size and style
custom_font = ("Arial", 12)

# Create labels and entry widgets with custom font
label_pokemon_name = tk.Label(window, text="Enter a Pokemon name:", font=custom_font)
entry_pokemon_name = tk.Entry(window, font=custom_font)

label_generation = tk.Label(window, text="Enter a generation number (1-9):", font=custom_font)
entry_generation = tk.Entry(window, font=custom_font)

label_pokedex_number = tk.Label(window, text="Enter a National Pokedex number:", font=custom_font)
entry_pokedex_number = tk.Entry(window, font=custom_font)

# Create buttons for options with custom font
button_get_data = tk.Button(window, text="Get data for a Pokemon", command=lambda: on_option_selected(1), font=custom_font)
button_display_generation = tk.Button(window, text="Display Pokemon by Generation", command=lambda: on_option_selected(2), font=custom_font)
button_search_by_pokedex = tk.Button(window, text="Search by National Pokedex Number", command=lambda: on_option_selected(3), font=custom_font)
button_get_random = tk.Button(window, text="Get data for a Random Pokemon", command=lambda: on_option_selected(4), font=custom_font)
button_quit = tk.Button(window, text="Quit", command=lambda: on_option_selected(5), font=custom_font)

# Arrange the widgets using the grid layout
label_pokemon_name.grid(row=0, column=0, padx=10, pady=5)
entry_pokemon_name.grid(row=0, column=1, padx=10, pady=5)
button_get_data.grid(row=0, column=2, padx=10, pady=5)

label_generation.grid(row=1, column=0, padx=10, pady=5)
entry_generation.grid(row=1, column=1, padx=10, pady=5)
button_display_generation.grid(row=1, column=2, padx=10, pady=5)

label_pokedex_number.grid(row=2, column=0, padx=10, pady=5)
entry_pokedex_number.grid(row=2, column=1, padx=10, pady=5)
button_search_by_pokedex.grid(row=2, column=2, padx=10, pady=5)

button_get_random.grid(row=3, column=0, padx=10, pady=5)
button_quit.grid(row=3, column=1, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()
