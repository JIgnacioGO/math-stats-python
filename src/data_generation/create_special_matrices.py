import numpy as np
from numpy.random import Generator
from typing import Literal, Tuple


def create_special_matrices(
        rng: Generator,
        matrix_type: Literal["random", "symmetric", "orthogonal", "singular", "diagonal"] = "random",
        size: Tuple[int, int] = (4, 4),
        condition_number: float = None
) -> np.ndarray:
    """
    Genera matrices con propiedades específicas para ejercicios teóricos.

    Esencial para problemas sobre determinantes, eigenvectores, invertibilidad, etc.

    Args:
        rng (Generator): El generador de números aleatorios de NumPy.
        matrix_type (str): 'random', 'symmetric', 'orthogonal', 'singular', 'diagonal'.
        size (tuple): Dimensiones (filas, columnas) de la matriz.
        condition_number (float): Si se especifica, ajusta el número de condición.

    Returns:
        np.ndarray: La matriz generada.
    """
    m, n = size

    if matrix_type == "random":
        matrix = rng.standard_normal(size)
    elif matrix_type == "symmetric":
        if m != n: raise ValueError("La matriz simétrica debe ser cuadrada.")
        A = rng.standard_normal((m, m))
        matrix = (A + A.T) / 2
    elif matrix_type == "orthogonal":
        if m != n: raise ValueError("La matriz ortogonal debe ser cuadrada.")
        A = rng.standard_normal((m, m))
        Q, _ = np.linalg.qr(A)
        matrix = Q
    elif matrix_type == "singular":
        if m != n: raise ValueError("Este método simple requiere una matriz cuadrada para garantizar la singularidad.")
        rank = min(m, n) - 1
        if rank <= 0: raise ValueError("El tamaño de la matriz es demasiado pequeño para crear una matriz singular.")
        U = rng.standard_normal((m, rank))
        V = rng.standard_normal((rank, n))
        matrix = U @ V
    elif matrix_type == "diagonal":
        diag_vals = rng.uniform(1, 10, min(m, n))
        matrix = np.zeros(size)
        np.fill_diagonal(matrix, diag_vals)
    else:
        raise ValueError(f"Tipo de matriz '{matrix_type}' no reconocido.")

    if condition_number and matrix_type in ["random", "symmetric"] and m == n:
        U, s, Vt = np.linalg.svd(matrix)
        s_new = np.linspace(condition_number, 1, len(s))
        matrix = U @ np.diag(s_new) @ Vt

    return np.round(matrix, 3)
