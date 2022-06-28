from FilePrioridade import *


fila = FilaPrioridade(4)
print("")

fila.is_empty(True)

fila.add(No("Luciana",1))       # 1
fila.add(No("Lívia", 0))        # 2
fila.add(No("Manoel", 3))       # 3
fila.add(No("Jenniffer", 1))    # 4
fila.add(No("Ana",3))           # 5
fila.add(No("Maria",5))         # 6 - Deverá exibir mensagem de erro
print("")

fila.list_items()
print("")

print("Removendo item da Fila!\n")
fila.remove()

fila.list_items()

fila.add(No("Maria", 5))
print("")
fila.list_items()

print("Removendo item da Fila!\n")
fila.remove()
fila.remove()
fila.remove()
fila.remove()
fila.remove()
fila.remove()
