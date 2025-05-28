import sys
from itertools import combinations

def solve():
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    points = []
    for _ in range(N):
        x = int(input[idx])
        y = int(input[idx + 1])
        points.append((x, y))
        idx += 2
    
    max_area = 0
    
    for trio in combinations(points, 3):
        a, b, c = trio
        # Verificar si hay un lado paralelo al eje x (misma y) y otro paralelo al eje y (misma x)
        # Caso 1: a y b tienen misma y (paralelo al eje x), a y c tienen misma x (paralelo al eje y)
        if (a[1] == b[1] and a[0] == c[0]):
            base = abs(a[0] - b[0])
            height = abs(a[1] - c[1])
            area = base * height
            if area > max_area:
                max_area = area
        # Caso 2: a y b tienen misma y, b y c tienen misma x
        elif (a[1] == b[1] and b[0] == c[0]):
            base = abs(a[0] - b[0])
            height = abs(b[1] - c[1])
            area = base * height
            if area > max_area:
                max_area = area
        # Caso 3: a y c tienen misma y, a y b tienen misma x
        elif (a[1] == c[1] and a[0] == b[0]):
            base = abs(a[0] - c[0])
            height = abs(a[1] - b[1])
            area = base * height
            if area > max_area:
                max_area = area
        # Caso 4: a y c tienen misma y, b y c tienen misma x
        elif (a[1] == c[1] and b[0] == c[0]):
            base = abs(a[0] - c[0])
            height = abs(b[1] - c[1])
            area = base * height
            if area > max_area:
                max_area = area
        # Caso 5: b y c tienen misma y, a y b tienen misma x
        elif (b[1] == c[1] and a[0] == b[0]):
            base = abs(b[0] - c[0])
            height = abs(a[1] - b[1])
            area = base * height
            if area > max_area:
                max_area = area
        # Caso 6: b y c tienen misma y, a y c tienen misma x
        elif (b[1] == c[1] and a[0] == c[0]):
            base = abs(b[0] - c[0])
            height = abs(a[1] - c[1])
            area = base * height
            if area > max_area:
                max_area = area
    
    print(max_area)

solve()
