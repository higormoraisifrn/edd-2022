# -*- coding:UTF-8 -*-

class No:
    """" Contrutor da Classe No"""
    def __init__(self, chave) -> None:
        self.chave = chave
        self.prox = -1 # ponteiro próx índice

    def __str__(self) -> str:
        return f"No(chave={self.chave}, prox={self.prox})"


