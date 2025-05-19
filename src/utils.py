"""
Módulo com funções auxiliares.
"""
import random
from typing import List

from src.model.ponto import Ponto


def gerar_pontos(n: int, limite: int = 1000) -> List[Ponto]:
    """
    Gera uma lista com n pontos aleatórios dentro de um intervalo.

    Parameters
    ----------
    n : int
        Número de pontos a serem gerados.
    limite : int
        Valor máximo (inclusive) para coordenadas x e y.

    Returns
    -------
    List[Ponto]
        Lista de objetos Ponto com coordenadas aleatórias.
    """
    return [Ponto(random.randint(0, limite), random.randint(0, limite)) for _ in range(n)]
