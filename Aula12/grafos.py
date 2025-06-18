
grafo = [
    1,2,3,
    4,5,6,
    7,8,9
]

# for i in range(len(grafo)):
#     print(grafo[i], end=' ')
#     if (i + 1) % 3 == 0:
#         print()

for i in range(0, len(grafo), 3):
    print(grafo[i], grafo[i+1], grafo[i+2])
