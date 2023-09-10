import requests
import random

class Pokemon:
    def __init__(self, name):
        """ Using the RESTful POKEMON API"""
        self.name = name
        self.stats = {}
    
    def fetch_data(self):
        # Build the URL to fetch data for the specified Pokemon from the PokéAPI
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        
        # Send an HTTP GET request to the PokéAPI
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            data = response.json()
            
            # Store the Pokemon's name and stats in the stats dictionary
            self.stats["Name"] = data["name"]
            for stat in data["stats"]:
                self.stats[stat["stat"]["name"]] = stat["base_stat"]
        else:
            # Handle the case where the request fails
            print(f"Failed to fetch data for {self.name}")
        print("")

    def display_stats(self):

        # Display the Pokemon's name and its stats
        print(f"Pokemon: {self.stats['Name']}")
        print("Stats:")
        for stat_name, stat_value in self.stats.items():
            if stat_name != "Name":
                print(f"{stat_name}: {stat_value}")
        print("")

# Function to display the names of Pokemon in a specific generation
def display_generation_pokemon(generation):
    # Build the URL to fetch data for the specified generation from the PokéAPI
    url = f"https://pokeapi.co/api/v2/generation/{generation}/"
    
    # Send an HTTP GET request to the PokéAPI
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        
        # Display the names of Pokemon in the specified generation
        print(f"Pokemon in Generation {generation}:")
        for pokemon in data["pokemon_species"]:
            print(pokemon['url'].split('/')[-2],":", pokemon["name"])
    else:
        # Handle the case where the request fails
        print(f"Failed to fetch Generation {generation} data")
    print("")

# Function to search for a Pokemon by National Pokedex number
def search_by_pokedex_number():
    pokedex_number = input("Enter a National Pokedex number: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_name = data["name"]
        
        # Create a Pokemon object and fetch data for the specified Pokemon
        pokemon = Pokemon(pokemon_name.lower())
        pokemon.fetch_data()
        pokemon.display_stats()
    else:
        print(f"No Pokemon found for National Pokedex number {pokedex_number}")
    print("")

# Function to fetch data for a random Pokemon
def fetch_random_pokemon():
    random_pokemon_id = random.randint(1, 898)  # There are 898 Pokemon in total
    pokemon_name = str(random_pokemon_id)
    
    # Create a Pokemon object and fetch data for the random Pokemon
    pokemon = Pokemon(pokemon_name)
    pokemon.fetch_data()
    pokemon.display_stats()

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Get data for a Pokemon")
        print("2. Display names of Pokemon in the Pokedex")
        print("3. Search by National Pokedex Number")
        print("4. Get data for a Random Pokemon")
        print("5. Quit")
        option = input("Enter your choice (1/2/3/4/5): ")
        
        if option == "1":
            pokemon_name = input("Enter a Pokemon name: ")
            pokemon = Pokemon(pokemon_name.lower())
            pokemon.fetch_data()
            pokemon.display_stats()
        elif option == "2":
            print("Display Pokemon by Generation:")
            while True:
                generation_option = input("Enter a generation number (1-9): ")
                if generation_option.isdigit():
                    generation_option = int(generation_option)
                    if 1 <= generation_option <= 9:
                        display_generation_pokemon(generation_option)
                        break
                    else:
                        print("Invalid generation number. Please enter a number between 1 and 9.")
                else:
                    print("Invalid input. Please enter a valid number.")
        elif option == "3":
            search_by_pokedex_number()
        elif option == "4":
            fetch_random_pokemon()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, 4, or 5.")
        print("")
