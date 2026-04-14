# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


def init(max_laps):
    """
    Crea y retorna un diccionario para almacenar hasta max_laps vueltas.
    """
    diccionario = {
        'max': max_laps,
        'times': [],
        'total': 0.0
    }
    return diccionario 
    # TODO: Implementar
    


def add_lap(timer, time):
    """
    Agrega una nueva vuelta con el tiempo especificado.
    Retorna el diccionario modificado.
    """
    timer["times"].append(time)
    timer["total"] += time
    return timer
    # TODO: Implementar


def count(timer):
    """
    Retorna el numero de vueltas agregadas.
    """
    return len(timer["times"])
    # TODO: Implementar
    pass


def cumulative_time(timer):
    """
    Retorna el tiempo acumulado de todas las vueltas.
    """
    return round(timer["total"], 2)
    # TODO: Implementar
    pass


def format_laps(timer):
    """
    Retorna una representacion en cadena de los tiempos.
    Formato: [t1, t2, t3, ..., tn]
    """
    return str(timer["times"])
    # TODO: Implementar
    pass


def fastest_lap(timer):
    """
    Retorna el tiempo mas rapido de cualquier vuelta.
    """
    return min(timer["times"])
    # TODO: Implementar
    pass


def fastest_multi_lap(timer, k):
    """
    Retorna el tiempo acumulado mas rapido de cualquier k vueltas consecutivas.
    """
    times = timer["times"]
    best = float("inf")

    for i in range(len(times) - k + 1):
        suma = sum(times[i:i+k])
        if suma < best:
            best = suma
    return best

    # TODO: Implementar
    


def longest_decreasing_streak(timer):
    """
    Retorna la longitud maxima de una secuencia de vueltas consecutivas
    donde los tiempos disminuyen estrictamente.
    """
    times = timer["times"]
    max_streak = 1
    current = 1

    for i in range(1, len(times)):
        if times[i] < times[i-1]:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 1
    
    return max_streak
    # TODO: Implementar
    


def main():
    # crear un cronometro para el record mundial de 100m de Usain Bolt,
    # dividiendo la carrera en 10 segmentos (o "vueltas")
    timer = init(10)
    timer = add_lap(timer, 1.85)
    timer = add_lap(timer, 1.02)
    timer = add_lap(timer, 0.91)
    timer = add_lap(timer, 0.87)
    timer = add_lap(timer, 0.85)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.83)
    timer = add_lap(timer, 0.90)

    # imprimir estadisticas
    print("numero de vueltas =", count(timer))                    # 10
    print("tiempo acumulado =", cumulative_time(timer))           # 9.69
    print("vuelta mas rapida =", fastest_lap(timer))              # 0.82
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))       # 4.14
    print("racha mas larga =", longest_decreasing_streak(timer))  # 6

    # imprimir tiempos
    # [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.9]
    print(format_laps(timer))


if __name__ == "__main__":
    main()
