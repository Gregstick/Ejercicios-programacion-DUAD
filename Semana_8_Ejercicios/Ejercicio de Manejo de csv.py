import csv

games_list = [
    {
        'Name': 'NBA2K26',
        'Genre': 'Sport',
        'Developer': 'Visual Concepts',
        'ESRB Rating': 'E',
    },
    {
        'Name': 'Alan Wake 2',
        'Genre': 'Thriller',
        'Developer': 'Remedy Entertainment',
        'ESRB Rating': 'M',
    },
    {
        'Name': 'Red Dead Redemption 2',
        'Genre': 'Open World',
        'Developer': 'Rockstar Games',
        'ESRB Rating': 'M',
    },
    {
        'Name': 'Marvel Spiderman 2',
        'Genre': 'Action',
        'Developer': 'Insomniac Games',
        'ESRB Rating': 'T',
    }            
]

games_headers = (
    'Name',
    'Genre',
    'Developer',
    'ESRB Rating',
)


def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def request_new_games():
    total = int(input("Ingrese el número de juegos que quiere ingresar: "))
    n = 1
    new = []
    while n <= total:
        print(f"Este es el juego número: {n} ")
        name = str(input("Escriba el nombre del juego: "))
        genre = str(input("Escriba el género del juego: "))
        developer = str(input("Escriba el nombre del desarrollador: "))
        esrb_rating = str(input("Escriba la clasificación ESRB: "))

        new_game = {
            'Name': name,
            'Genre': genre,
            'Developer': developer,
            'ESRB Rating': esrb_rating,
        }

        new.append(new_game)
        n += 1
    return new




def add_new_games():
    new_game = request_new_games()
    games_list.extend(new_game)
    print(games_list)
    write_csv_file(
        'C:\\Users\\grego\\OneDrive\\Escritorio\\Greg\\LYFTER Programación\\Semana 8 Ejercicios.py\\games.csv', 
        games_list, 
        games_headers)


add_new_games()