import numpy as np
import pandas as pd
from numpy.random import Generator


def create_business_data(rng: Generator, simplified: bool = False, n_samples: int = 100) -> pd.DataFrame:
    """
    Genera un dataset de rendimiento de productos en un contexto de negocio.

    Ideal para ejercicios sobre regresión, análisis de características y OLS.

    Args:
        rng (Generator): El generador de números aleatorios de NumPy.
        simplified (bool): Si True, devuelve solo 'precio' y 'ventas_mensuales'.
        n_samples (int): Número de productos a generar.

    Returns:
        pd.DataFrame: Dataset de productos/ventas.
    """
    # 1. Variables predictoras
    precio = rng.uniform(10, 500, n_samples)
    gasto_marketing = rng.uniform(100, 5000, n_samples)
    calificacion_cliente = rng.uniform(1, 5, n_samples)
    competencia_precio = precio * rng.uniform(0.8, 1.3, n_samples)

    # 2. Variable objetivo con relaciones realistas
    ventas_mensuales = (
            1000 - 2 * precio +  # Precio más alto, menos ventas
            0.5 * gasto_marketing +  # Marketing aumenta ventas
            200 * calificacion_cliente +  # Calificación mejora ventas
            -0.3 * competencia_precio +  # Competencia reduce ventas
            rng.normal(0, 100, n_samples)
    ).clip(0, None)

    # 3. Ensamblaje del DataFrame
    dataset = pd.DataFrame({
        'precio': np.round(precio, 2),
        'gasto_marketing': np.round(gasto_marketing, 0),
        'calificacion_cliente': np.round(calificacion_cliente, 2),
        'competencia_precio': np.round(competencia_precio, 2),
        'ventas_mensuales': np.round(ventas_mensuales, 0).astype(int)
    })

    if simplified:
        return dataset[['precio', 'ventas_mensuales']]

    return dataset
