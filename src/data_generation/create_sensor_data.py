import numpy as np
import pandas as pd
from numpy.random import Generator


def create_sensor_data(rng: Generator, simplified: bool = False, n_samples: int = 200) -> pd.DataFrame:
    """
    Genera datos de sensores IoT con patrones temporales y cíclicos.

    Perfecto para ejercicios que involucran relaciones no lineales.

    Args:
        rng (Generator): El generador de números aleatorios de NumPy.
        simplified (bool): Si True, devuelve solo 'temperatura' y 'consumo_energia'.
        n_samples (int): Número de mediciones a generar.

    Returns:
        pd.DataFrame: Dataset de sensores.
    """
    # 1. Simulación de ciclo diario
    hours = np.linspace(0, 24, n_samples)

    # 2. Variables con patrones temporales
    temperatura = 20 + 10 * np.sin(2 * np.pi * hours / 24) + rng.normal(0, 1.5, n_samples)
    humedad = 60 - 0.5 * temperatura + rng.normal(0, 5, n_samples)
    presion_atmosferica = 1013 + rng.normal(0, 5, n_samples)
    velocidad_viento = np.abs(rng.normal(5, 3, n_samples))

    # 3. Consumo de energía relacionado con temperatura (no lineal)
    consumo_energia = (
            100 +
            2 * np.maximum(temperatura - 22, 0) +  # Aire acondicionado
            1.5 * np.maximum(18 - temperatura, 0) +  # Calefacción
            0.1 * humedad +
            rng.normal(0, 10, n_samples)
    ).clip(50, None)

    # 4. Ensamblaje del DataFrame
    dataset = pd.DataFrame({
        'hora': np.round(hours, 2),
        'temperatura': np.round(temperatura, 1),
        'humedad': np.round(humedad, 1),
        'presion_atmosferica': np.round(presion_atmosferica, 1),
        'velocidad_viento': np.round(velocidad_viento, 1),
        'consumo_energia': np.round(consumo_energia, 1)
    })

    if simplified:
        return dataset[['temperatura', 'consumo_energia']]

    return dataset
