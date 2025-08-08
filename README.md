# Repositorio de Fundamentos de Matemáticas y Estadística para Ciencia de Datos

``(EN CONSTRUCCIÓN)`` Este repositorio contiene una serie de Jupyter Notebooks que exploran los conceptos fundamentales de matemáticas y estadística aplicados a la ciencia de datos, utilizando principalmente SageMath y otras librerías del ecosistema de Python.

---
## Estructura del Repositorio

El proyecto está organizado de la siguiente manera:
-   **/notebooks**: Contiene todos los Jupyter Notebooks, organizados por área temática (Álgebra Lineal, Cálculo, Estadística Descriptiva, etc.).
-   **/data**: Contiene los datasets utilizados en los análisis.
-   **/src**: Contiene código fuente reutilizable o funciones auxiliares.
-   **/reports**: Contiene los Jupyter Notebooks resueltos, en formato ``pdf``.

---
## Requisitos Previos

Para poder ejecutar este proyecto, necesitarás tener instalado [Miniforge](https://github.com/conda-forge/miniforge) o cualquier otra distribución de Conda/Mamba.

> ### **Nota Importante para Usuarios de Windows**
>
> El entorno de este proyecto depende de **SageMath**, cuyo soporte nativo en Windows es limitado. La forma recomendada y oficial de trabajar con SageMath en Windows es a través del **Subsistema de Windows para Linux (WSL)**.
>
> Por favor, asegúrate de tener [WSL instalado y configurado](https://learn.microsoft.com/es-es/windows/wsl/install) en tu sistema. Todos los comandos de la sección "Instalación y Configuración" deben ser ejecutados **dentro de una terminal de WSL (como Ubuntu)**, no en PowerShell o CMD.

---
## Instalación y Configuración

Sigue estos pasos para configurar el entorno y poder ejecutar los notebooks:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/JIgnacioGO/math-stats-python
    ```
2.  **Navega a la carpeta del proyecto:**
    ```bash
    cd math-stats-python
    ```
3.  **Crea el entorno de Conda desde el archivo `environment.yml`:**
    Este comando creará un entorno llamado `sagemath-env` con todas las dependencias exactas necesarias para el proyecto.
    ```bash
    mamba env create -f environment.yml
    ```
4.  **Activa el nuevo entorno:**
    ```bash
    mamba activate sagemath-env
    ```
¡Listo! Ahora tienes todo lo necesario para ejecutar los notebooks.

---
## Uso

Una vez activado el entorno `sagemath-env`, puedes abrir los notebooks usando tu herramienta preferida:
-   **Jupyter Lab:**
    ```bash
    jupyter lab
    ```
-   **Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
-   O abriendo la carpeta del proyecto con un IDE como **DataSpell** o **VS Code**.

---
## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.