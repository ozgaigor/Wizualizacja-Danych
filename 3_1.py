listaA = [1/x for x in range(1,11)]
print("listaA", listaA)
listaB = [2 ** x for x in range(1,11)]
print("listaB", listaB)
listaC = [x for x in listaB if x % 4 == 0]
print("listaC", listaC)