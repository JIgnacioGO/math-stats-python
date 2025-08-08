import pandas as pd
import numpy as np
import os
from typing import Union


def save_dataset(dataset: Union[pd.DataFrame, np.ndarray],
                 project_root: str,
                 filename: str,
                 folder: str = "data/raw"):
    """
    Guarda un DataFrame o un array de NumPy en la estructura de carpetas del proyecto.

    Args:
        dataset (Union[pd.DataFrame, np.ndarray]): El dataset a guardar.
        project_root (str): La ruta absoluta a la raíz del proyecto.
        filename (str): El nombre del archivo (e.g., 'my_data.csv').
        folder (str): La subcarpeta dentro del proyecto (e.g., 'data/raw').
    """
    save_path = os.path.join(project_root, folder)
    os.makedirs(save_path, exist_ok=True)
    filepath = os.path.join(save_path, filename)

    if isinstance(dataset, pd.DataFrame):
        dataset.to_csv(filepath, index=False)
    elif isinstance(dataset, np.ndarray):
        np.savetxt(filepath, dataset, delimiter=',')
    else:
        raise TypeError("El dataset debe ser un DataFrame de pandas o un array de NumPy.")

    print(f"Dataset guardado en: {filepath}")


def load_dataset(project_root: str,
                 filename: str,
                 folder: str = "data/raw") -> pd.DataFrame:
    """
    Carga un dataset desde la estructura de carpetas del proyecto.

    Args:
        project_root (str): La ruta absoluta a la raíz del proyecto.
        filename (str): El nombre del archivo a cargar.
        folder (str): La subcarpeta dentro del proyecto.

    Returns:
        pd.DataFrame: El dataset cargado.
    """
    filepath = os.path.join(project_root, folder, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo en: {filepath}")
    return pd.read_csv(filepath)
