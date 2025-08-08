import numpy as np
import pandas as pd
from numpy.random import Generator
from typing import Literal


def create_edge_cases(
        rng: Generator,
        case_type: Literal["multicollinear", "outliers", "missing_values", "nonlinear"] = "multicollinear",
        n_samples: int = 100
) -> pd.DataFrame:
    """
    Genera datasets con características especiales para casos de borde.

    Prepara a los estudiantes para desafíos del mundo real en modelado.

    Args:
        rng (Generator): El generador de números aleatorios de NumPy.
        case_type (str): 'multicollinear', 'outliers', 'missing_values', 'nonlinear'.
        n_samples (int): Número de muestras a generar.

    Returns:
        pd.DataFrame: El dataset con características especiales.
    """
    if case_type == "multicollinear":
        x1 = rng.normal(0, 1, n_samples)
        x2 = x1 + rng.normal(0, 0.1, n_samples)
        x3 = 2 * x1 - 1.5 * x2 + rng.normal(0, 0.2, n_samples)
        y = x1 + x2 + x3 + rng.normal(0, 0.5, n_samples)
        return pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'y': y})

    elif case_type == "outliers":
        x = rng.normal(10, 2, n_samples)
        y = 2 * x + rng.normal(0, 1, n_samples)
        outlier_idx = rng.choice(n_samples, n_samples // 20, replace=False)  # 5% outliers
        x[outlier_idx] = rng.uniform(50, 100, len(outlier_idx))
        y[outlier_idx] = rng.uniform(-50, -20, len(outlier_idx))
        return pd.DataFrame({'x': x, 'y': y})

    elif case_type == "missing_values":
        data = rng.standard_normal((n_samples, 4))
        df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
        for col in ['B', 'C']:
            missing_idx = rng.choice(n_samples, n_samples // 10, replace=False)  # 10% missing
            df.loc[missing_idx, col] = np.nan
        return df

    elif case_type == "nonlinear":
        x = np.linspace(-3, 3, n_samples)
        y = np.sin(x * np.pi) + x ** 2 + rng.normal(0, 0.3, n_samples)
        return pd.DataFrame({'x': x, 'y': y})

    else:
        raise ValueError(f"Tipo de caso especial '{case_type}' no reconocido.")
