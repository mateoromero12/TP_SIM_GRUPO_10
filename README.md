# TP_SIM_GRUPO_10
Repositorio del grupo 10 para el desarrollo de la materia Simulación en el curso 4K2 de la Universidad Tecnológica Nacional - Facultad Regional Córdoba en el año 2025

## Trabajo Práctico de Laboratorio 2
Este proyecto incluye un archivo llamado `tpl2_sim.py`, el cual implementa un aplicativo para la generación y análisis de variables aleatorias según diferentes distribuciones estadísticas. Esta se ejecuta en consola para la generación y visualización de variables aleatorias según diferentes distribuciones. 

1. **Generación de Variables Aleatorias**:
    - Permite generar variables aleatorias de 4 dígitos decimales para las siguientes distribuciones:
      - **Uniforme [a, b]**: Genera variables aleatorias dentro de un rango definido por el usuario.
      - **Exponencial**: Utiliza un parámetro de tasa (lambda) ingresado por el usuario.
      - **Normal**: Requiere la media y la desviación estándar como parámetros.

2. **Tamaño de Muestra**:
    - El usuario puede especificar el tamaño de la muestra, con un límite máximo de 1.000.000 valores.

3. **Visualización de Datos**:
    - La serie generada puede visualizarse directamente en la consola o en un archivo de salida.

4. **Análisis de Frecuencias**:
    - Genera un histograma de frecuencias para la serie de variables aleatorias.
    - Permite seleccionar entre 10, 15, 20 o 25 intervalos para el histograma.
    - Incluye una tabla de frecuencias con los límites de los intervalos y las frecuencias observadas.

5. **Gráficos Informativos**:
    - El histograma incluye rótulos en los ejes, límites de los intervalos y valores de frecuencia para facilitar la interpretación.

    ### ¿Cómo Ejecutar el Script?

    Para ejecutar el archivo `tpl2_sim.py`, sigue los siguientes pasos:

    1. **Requisitos Previos**:
        - Asegúrate de tener Python 3.8 o superior instalado en tu sistema.
        - Instala las dependencias necesarias ejecutando:
          ```bash
          pip install -r requirements.txt
          ```

    2. **Ejecución del Script**:
        - Abre una terminal o consola en el directorio donde se encuentra el archivo `tpl2_sim.py`.
        - Ejecuta el script con el siguiente comando:
          ```bash
          python tpl2_sim.py
          ```

    3. **Interacción**:
        - Sigue las instrucciones que aparecerán en la consola para seleccionar la distribución, ingresar los parámetros y definir el tamaño de la muestra.

    4. **Salida de Resultados**:
        - Los resultados se mostrarán en la consola, a excepción del histograma, que se abrirá en una ventana emergente.
