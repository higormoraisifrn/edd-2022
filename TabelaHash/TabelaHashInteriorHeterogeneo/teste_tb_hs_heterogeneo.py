from tb_hash_encad_int_heterogeneo import TabelaHashInteriorHeterogeno
from no import No

tb = TabelaHashInteriorHeterogeno()

tb.inserir(No(48))
tb.inserir(No(3))
tb.inserir(No(80))
tb.inserir(No(31))
tb.inserir(No(20))
tb.inserir(No(2))
tb.inserir(No(1))

print("\t\t ---> TODA A LISTA PREENCHIDA")
tb.imprimir()

tb.remover(80)
tb.remover(3)

print("\t\t ---> LISTA SEM 80 E 3")
tb.imprimir()

tb.inserir(No(7))

tb.imprimir()

tb.remover(31)

print("\t\t ---> LISTA SEM 31")
tb.imprimir()

print("\t\t ---> SE ACABOU...")