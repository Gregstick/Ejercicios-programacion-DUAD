def write_text_to_file(path):
    try:
        with open("Semana 8 Ejercicios.py/songnames.txt", "r", encoding="utf-8") as file:
            songs = file.readlines()
    except FileNotFoundError:
        print("Ocurrió un error: el archivo no se encontró")    

    songs = [c.strip() for c in songs if c.strip()]
    sorted_songs = sorted(songs)
    for song in sorted_songs:
        print(f"Linea: {song}")

    try:
        with open("Semana 8 Ejercicios.py/songnamessorted.txt", "w", encoding="utf-8") as new_file:
            for song in sorted_songs:
                new_file.write(song + "\n")
    except Exception:
        print("Ocurrió un error: No tienes los permisos para escribir este archivo")



write_text_to_file("Semana 8 Ejercicios.py/songnames.txt")
