from No import *

class FilaPrioridade:
    def __init__(self, capacity=10) -> None:
        self._capacity = capacity
        self._head = None
        self._size = 0
        print(f"Criada Fila de Prioridade com capacidade {self._capacity}")


    def is_empty(self, print_str=False):
        if print_str:
            print("A fila está VAZIA!")
        return True if self._head is None else False

    
    def is_full(self, print_str=False):
        if print_str:
            print("A fila está Cheia!")
        return True if self._size == self._capacity else False


    def add(self, node):

        # 1º caso
        if self.is_empty():
            self._head = node
            self._size += 1
            print(f"Adicionado ({node} : valor-prioridade)")
        else:
            # 2º caso
            if self.is_full():
                print("A fila está Cheia!")
            else:
                iterator = self._head

                # inserindo na cabeça da fila
                # 3º caso (início da fila)
                if node.priority() > iterator.priority():
                    node.next = iterator
                    self._head = node
                # 4º caso (inserção no meio ou no fim da fila)
                else:
                    # iteração na fila
                    while iterator.next is not None and node.priority() <= iterator.next.priority():
                        iterator = iterator.next
                    
                    node.next = iterator.next
                    iterator.next = node
                
                self._size += 1
                print(f"Adicionado ({node} : valor-prioridade)")


    def remove(self):
        if not self.is_empty():
            removed = self._head
            self._head = removed.next
            self._size -= 1
            print(f"Removendo ({removed} : prioridade-valor)")
        else:
            print ("Fila VAZIA. Impossível remover!")

    
    def list_items(self):
        iterator = self._head
        if not self.is_empty():
            print("Elementos da Fila:")
            while iterator is not None:
                print(f"Item: {iterator}")
                iterator = iterator.next
        else:
            print("Fila VAZIA. Não há o que exibir!")