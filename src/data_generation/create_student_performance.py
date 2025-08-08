import numpy as np
import pandas as pd
from numpy.random import Generator


def create_student_performance_data(rng: Generator, simplified: bool = False, n_samples: int = 100) -> pd.DataFrame:
    """
    Genera un dataset sintético de rendimiento estudiantil.

    Este es el dataset del "Hilo Conductor", diseñado para ser el ejemplo
    principal a lo largo de los notebooks.

    Args:
        rng (Generator): El generador de números aleatorios de NumPy.
        simplified (bool): Si es True, devuelve solo 'horas_estudio' y
                           'calificacion_examen'. Por defecto es False.
        n_samples (int): El número de estudiantes (filas) a generar.

    Returns:
        pd.DataFrame: El dataset generado.
    """
    # 1. Generación de Variables Predictoras
    horas_estudio = rng.normal(loc=10, scale=4, size=(n_samples, 1)).clip(1, 25)
    calificacion_previa = (60 + horas_estudio * 0.5 + rng.normal(0, 10, (n_samples, 1))).clip(30, 100)
    asistencia_porcentaje = rng.normal(loc=90, scale=8, size=(n_samples, 1)).clip(50, 100)
    tutor_privado = rng.choice([0, 1], size=(n_samples, 1), p=[0.7, 0.3])

    # 2. Modelado de la Variable Objetivo
    coef_horas, coef_previa, coef_asistencia, coef_tutor, intercepto = 2.0, 0.3, 0.15, 5.0, 5

    calificacion_examen = (intercepto +
                           coef_horas * horas_estudio +
                           coef_previa * calificacion_previa +
                           coef_asistencia * asistencia_porcentaje +
                           coef_tutor * tutor_privado +
                           rng.normal(loc=0, scale=5, size=(n_samples, 1)))
    calificacion_examen = calificacion_examen.clip(20, 100)

    # 3. Ensamblaje del DataFrame
    dataset = pd.DataFrame({
        'horas_estudio': np.round(horas_estudio.flatten(), 1),
        'calificacion_previa': np.round(calificacion_previa.flatten(), 1),
        'asistencia_porcentaje': np.round(asistencia_porcentaje.flatten(), 1),
        'tutor_privado': tutor_privado.flatten(),
        'calificacion_examen': np.round(calificacion_examen.flatten(), 1)
    })

    if simplified:
        return dataset[['horas_estudio', 'calificacion_examen']]

    return dataset
