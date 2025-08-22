import json

pokemon_list = [
    {
    "name": {
        "english": "Pikachu"
    },
    "type": [
        "Electric"
    ],
    "base": {
        "HP": 35,
        "Attack": 55,
        "Defense": 40,
        "Sp. Attack": 50,
        "Sp. Defense": 50,
        "Speed": 90
    }
    },
    {
    "name": {
        "english": "Charmander"
    },
    "type": [
        "Fire"
    ],
    "base": {
        "HP": 39,
        "Attack": 52,
        "Defense": 43,
        "Sp. Attack": 60,
        "Sp. Defense": 50,
        "Speed": 65
    }
    },
    {
    "name": {
        "english": "Squirtle"
    },
    "type": [
        "Water"
    ],
    "base": {
        "HP": 44,
        "Attack": 48,
        "Defense": 65,
        "Sp. Attack": 50,
        "Sp. Defense": 64,
        "Speed": 43
    }
    }
]


def sorted_pokemon_list():
    with open('Pokemonlist.json', 'w') as file:
        json.dump(pokemon_list, file, indent=4, sort_keys=True)
    
"""with open('Pokemonlist.json', 'r') as read_file:
    read_data = json.load(read_file)
    print(read_data)"""

def original_pokemon_list():
    with open('Pokemonlist.json', 'r') as database_file:
        read_database_file = json.load(database_file)
        print(read_database_file)
        for pokemon in read_database_file:
            for key, value in pokemon.items():
                print(f'{key}, {value}')

def add_new_pokemon():
    name = str(input("Ingresa el nombre del nuevo pokemon: "))
    type = str(input("Ingresa el tipo de pokemon que es: "))
    hp = int(input("Ingresa el valor de HP del pokemon: "))
    attack = int(input("Ingresa el valor de ataque del pokemon: "))
    defense = int(input("Ingresa el valor de defensa del pokemon: "))
    sp_attack = int(input("Ingresa el valor de ataque especial del pokemon: "))
    sp_defense = int(input("Ingresa el valor de defensa especial del pokemon: "))
    speed = int(input("Ingresa el valor de velocidad del pokemon: "))

    new_pokemon = {
        "name" : {
            "english" : name
        },
        "type" : [type],
        "base" : {
            "HP" : hp,
            "Attack" : attack,
            "Defense" : defense,
            "Sp. Attack" : sp_attack,
            "Sp. Defense" : sp_defense,
            "Speed" : speed
        }
}
    
    return new_pokemon

def main():
    original_pokemon_list()
    new_pokemon = add_new_pokemon()
    pokemon_list.append(new_pokemon)
    print(pokemon_list)
    sorted_pokemon_list()



main()