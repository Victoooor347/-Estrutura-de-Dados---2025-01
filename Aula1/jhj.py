
def read_vector():
    return [3, 6, 2, 4, 8]

    # vector = []
    #
    # while len(vector) < 5:
    #     value = int(input("> Digite um valor: "))
    #     vector.append(value)
    #
    # return vector

def show_vector(vector):
    for i in range(len(vector)):
        print(vector[i])

def show_pairs(vector):
    for i in range(len(vector)):
        if vector[i] % 2 == 0:
            print(vector[i])

def show_max_and_min(vector):
    max_num = vector[0]
    min_num = vector[0]

    for i in range(len(vector)):
        if vector[i] > max_num:
            max_num = vector[i]
        if vector[i] < min_num:
            min_num = vector[i]

    print(f"Maior número: {max_num}")
    print(f"Menor número: {min_num}")

def bubble_sort(vector):
    for i in range(len(vector)):
        for j in range(len(vector) - 1):
            if vector[j] > vector[j + 1]:
                aux = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = aux


    print(vector)

values = read_vector()

print("Todos valores: ")
show_vector(values)

print("Valores pares: ")
show_pairs(values)

show_max_and_min(values)

bubble_sort(values)