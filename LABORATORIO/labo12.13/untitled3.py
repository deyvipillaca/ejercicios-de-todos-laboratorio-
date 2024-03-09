from collections import deque

class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.visitados = set()

    def bfs(self, inicio, destino):
        cola = deque([(inicio, [])])

        while cola:
            actual, camino = cola.popleft()
            fila, columna = actual

            if actual == destino:
                return camino + [actual]

            if actual in self.visitados:
                continue

            self.visitados.add(actual)

            for vecino in [(fila-1, columna), (fila+1, columna), (fila, columna-1), (fila, columna+1)]:
                vecino_fila, vecino_columna = vecino
                if 0 <= vecino_fila < self.filas and 0 <= vecino_columna < self.columnas and self.laberinto[vecino_fila][vecino_columna] != '#':
                    cola.append((vecino, camino + [actual]))

laberinto = [
    ['#', 'S', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', 'E', '#'],
    ['#', '#', '#', '#', '#']
]

lab = Laberinto(laberinto)
inicio = (0, 1)  # Coordenadas del punto de inicio
destino = (3, 3)  # Coordenadas del punto de destino

camino_mas_corto = lab.bfs(inicio, destino)

if camino_mas_corto:
    print("Camino más corto encontrado:")
    for paso in camino_mas_corto:
        print(paso)
else:
    print("No se encontró un camino válido.")
