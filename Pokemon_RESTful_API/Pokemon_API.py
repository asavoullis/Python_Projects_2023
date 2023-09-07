import requests

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

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Get data for a Pokemon")
        print("2. Display names of Pokemon in the Pokedex")
        print("3. Quit")
        option = input("Enter your choice (1/2/3): ")
        
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
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
