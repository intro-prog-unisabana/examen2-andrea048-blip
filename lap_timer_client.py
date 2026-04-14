# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    
    name_archivo = input("Ingrese el nombre del archivo: ")
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    
    with open(name_archivo, "r") as file:
        n = int(file.readline().strip())
        cronometro = lap_timer.init(n)
        for _ in range(n):
            tiempo = float(file.readline().strip())
            cronometro = lap_timer.add_lap(cronometro, tiempo)
    racha_min = lap_timer.longest_decreasing_streak(cronometro)
    print(racha_min)
    



if __name__ == "__main__":
    main()
