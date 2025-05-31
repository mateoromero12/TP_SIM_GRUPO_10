import random
import numpy as np
from math import pi
from typing import List, Tuple

def generate_uniform_distribution(sample_size: int, precision: int, a: float, b: float) -> List[float]:
    """
    Genera variables aleatorias con distribución uniforme en el intervalo [a, b).
    """
    return [round(a + random.random() * (b - a), precision) for _ in range(sample_size)]


def generate_exponential_distribution(sample_size: int, precision: int, lambda_val: float) -> List[float]:
    """
    Genera números aleatorios con distribución exponencial usando lambda.
    """
    return [round(-np.log(1 - random.random()) / lambda_val, precision) for _ in range(sample_size)]


def generate_normal_distribution(sample_size: int, precision: int, mean: float, std_dev: float) -> List[float]:
    """
    Genera números aleatorios con distribución normal (media y desviación estándar).
    Usa el método de Box-Muller.
    """
    random_numbers = []
    for _ in range((sample_size + 1) // 2):
        n1, n2 = generate_normal_random(mean, std_dev)
        random_numbers.extend([round(n1, precision), round(n2, precision)])
        if len(random_numbers) >= sample_size:
            break
    return random_numbers[:sample_size]


def generate_normal_random(mean: float, std_dev: float) -> Tuple[float, float]:
    """
    Genera dos números aleatorios con distribución normal usando el método Box-Muller.
    """
    u1 = random.random()
    u2 = random.random()
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * pi * u2)
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * pi * u2)
    return mean + z1 * std_dev, mean + z2 * std_dev
