# -*- coding:UTF-8 -*-
from enum import Enum


# Constantes
OCUPADO = 1
VAZIO = -1
LIBERADO = -2


class TabelaHashInteriorHeterogeno:
    """" Contrutor da Classe TabelaHash"""
    def __init__(self, p=4, s=3) -> None:
        self.tamanho = p+s
        self.p = p
        self.slot = self.tamanho*[None]
        self.status = self.tamanho*[VAZIO]


    def hash_function(self, chave):
        return chave % self.p


    def buscar(self, chave):
        posicao = self.hash_function(chave)
        achou = True

        # verifica posicao disponível na lista de palavras
        if self.status[posicao] == VAZIO:
            return not achou, posicao
        else:
            # iterar sobre a Tabela
            while True:
                if self.slot[posicao].chave == chave:
                    return achou, posicao
                else:
                    # verifica se há um próximo a ser verificado
                    if self.slot[posicao].prox != VAZIO:
                        posicao = self.slot[posicao].prox
                    else:
                        return not achou, posicao


    def inserir(self, node):
        index = self.hash_function(node.chave)
        sinonimo = False

        # inserir na parte "p" da Tabela
        if self.status[index] != OCUPADO:
            if self.status[index] == LIBERADO:
                node.prox = self.slot[index].prox
            self.slot[index] = node
            self.status[index] = OCUPADO
        else:
            aux_index = index
            anterior = index
            continua = True

            # Verifica se tem sinônimo
            if self.slot[aux_index].prox != VAZIO:
                sinonimo = True

            if sinonimo:
                while continua:
                    anterior = aux_index
                    if self.slot[aux_index].prox != -1:
                        aux_index = self.slot[aux_index].prox
                    else:
                        while self.status[aux_index] == OCUPADO and aux_index<self.tamanho:
                            aux_index += 1
                        continua = False
            else:
                aux_index = self.p
                while self.status[aux_index] == OCUPADO and aux_index<self.tamanho:
                    aux_index += 1
            
            # encontrou posição disponível na tabela
            if self.status[aux_index] != OCUPADO:
                self.slot[anterior].prox = aux_index
                if self.status[aux_index] == LIBERADO:
                    node.prox = self.slot[aux_index].prox
                self.slot[aux_index] = node
                self.status[aux_index] = OCUPADO
            else:
                print(f"Não foi possível inserir {node.chave} na Tabela")
        

    def remover(self, chave):
        achou, posicao = self.buscar(chave)

        if achou:
            self.status[posicao] = LIBERADO
        else:
            print(f"Chave {chave} não encontrada")


    def imprimir(self):
        posicao = 0
        for item in self.slot:
            if self.status[posicao] == OCUPADO:
                print(f"Posição: {posicao} --> Item: {item.chave}")
            else:
                print(f"Posição: {posicao} --> VAZIO/LIBERADO")
            posicao += 1

    