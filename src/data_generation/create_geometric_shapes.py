import numpy as np
import pandas as pd
from numpy.random import Generator
from typing import Literal


def create_geometric_shapes(
        rng: Generator,
        shape_type: Literal["circle", "ellipse", "line", "parabola", "spiral"] = "circle",
        n_samples: int = 50,
        noise_level: float = 0.1
) -> pd.DataFrame:
    """
    Genera puntos 2D que siguen formas geométricas específicas.

    Fundamental para ejercicios de visualización de transformaciones lineales,
    bases, span y proyecciones.

    Args:
        rng (Generator): El generador de números aleatorios de NumPy.
        shape_type (str): 'circle', 'ellipse', 'line', 'parabola', 'spiral'.
        n_samples (int): Número de puntos a generar.
        noise_level (float): Cantidad de ruido gaussiano a añadir.

    Returns:
        pd.DataFrame: Coordenadas x, y de los puntos y la forma.
    """
    if shape_type == "circle":
        angles = np.linspace(0, 2 * np.pi, n_samples)
        radius = 5
        x, y = radius * np.cos(angles), radius * np.sin(angles)
    elif shape_type == "ellipse":
        angles = np.linspace(0, 2 * np.pi, n_samples)
        a, b = 8, 3  # Semi-ejes
        x, y = a * np.cos(angles), b * np.sin(angles)
    elif shape_type == "line":
        x = np.linspace(-10, 10, n_samples)
        y = 2 * x + 1
    elif shape_type == "parabola":
        x = np.linspace(-5, 5, n_samples)
        y = x ** 2
    elif shape_type == "spiral":
        t = np.linspace(0, 4 * np.pi, n_samples)
        x, y = t * np.cos(t), t * np.sin(t)
    else:
        raise ValueError(f"Tipo de forma '{shape_type}' no reconocido.")

    # Añadir ruido
    x += rng.normal(0, noise_level, n_samples)
    y += rng.normal(0, noise_level, n_samples)

    return pd.DataFrame({
        'x': np.round(x, 3),
        'y': np.round(y, 3),
        'shape': shape_type
    })
