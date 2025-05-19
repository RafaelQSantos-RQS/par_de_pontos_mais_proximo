"""
Módulo que representa um ponto em um plano cartesiano.

Classes:
    Ponto: Representa um ponto em um plano cartesiano.
"""

class Ponto:
    """
    Representa um ponto em um plano cartesiano.

    Attributes
    ----------
    x : int or float
        A coordenada x do ponto.
    y : int or float
        A coordenada y do ponto.
    """
    def __init__(self, x:int, y:int) -> None:
        """ 
        Inicializa o ponto com coordenadas x e y.
        """
        self.x:int = x
        self.y:int = y

    def __str__(self) -> str:
        """ 
        Retorna uma string representando o ponto em notacao de coordenadas
        cartesianas, ex. (2, 3).
        """
        return f'({self.x}, {self.y})'

    def distancia(self, ponto:'Ponto') -> float:
        """
        Calcula a distância euclidiana entre este ponto e outro ponto fornecido.

        Parameters
        ----------
        ponto : Ponto
            O outro ponto com o qual calcular a distância.

        Returns
        -------
        float
            A distância euclidiana entre os dois pontos.
        """
        return ((self.x - ponto.x)**2 + (self.y - ponto.y)**2)**0.5
