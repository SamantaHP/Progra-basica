def max_x_mowing(n, instructions):
    # Dirección: (dx, dy)
    direction_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

    x, y = 0, 0  # posición inicial
    time = 0
    last_visited = {}  # (x, y) -> tiempo en que se visitó por última vez
    max_x = float('inf')  # Buscamos el mínimo valor de x que mantenga válida la observación

    for d, s in instructions:
        dx, dy = direction_map[d]
        for _ in range(s):
            x += dx
            y += dy
            time += 1
            if (x, y) in last_visited:
                delta = time - last_visited[(x, y)]
                max_x = min(max_x, delta)
            last_visited[(x, y)] = time

    return max_x if max_x != float('inf') else -1


# Ejemplo de uso con la entrada de muestra del problema
entrada = [('N', 10), ('E', 2), ('S', 3), ('W', 4), ('S', 5), ('E', 8)]

n = len(entrada)
resultado = max_x_mowing(n, entrada)
print(resultado)
# Debería imprimir 10
