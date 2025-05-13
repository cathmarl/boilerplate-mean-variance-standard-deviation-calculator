import numpy as np

def calculate(list):
    if len(list) != 9:
         raise ValueError("List must contain nine numbers.")  # Cambié el mensaje a inglés
    # Convierte la lista en una matriz 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calcula los resultados
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Media por columna
            matrix.mean(axis=1).tolist(),  # Media por fila
            matrix.mean().tolist()         # Media de toda la matriz
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Varianza por columna
            matrix.var(axis=1).tolist(),   # Varianza por fila
            matrix.var().tolist()          # Varianza de toda la matriz
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Desviación estándar por columna
            matrix.std(axis=1).tolist(),   # Desviación estándar por fila
            matrix.std().tolist()          # Desviación estándar de toda la matriz
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Máximo por columna
            matrix.max(axis=1).tolist(),   # Máximo por fila
            matrix.max().tolist()          # Máximo de toda la matriz
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Mínimo por columna
            matrix.min(axis=1).tolist(),   # Mínimo por fila
            matrix.min().tolist()          # Mínimo de toda la matriz
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Suma por columna
            matrix.sum(axis=1).tolist(),   # Suma por fila
            matrix.sum().tolist()          # Suma de toda la matriz
        ]
    }
    
    return calculations
