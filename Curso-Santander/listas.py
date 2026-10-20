#Criação e Acesso

cores = ["Verde", "Branco", "Grená"]

print(cores[0])  # Acessando o primeiro elemento
print(cores[1])  # Acessando o segundo elemento 
print(cores[2])  # Acessando o terceiro elemento

print("")

#Acessando o último elemento da lista

print(cores[-1])  # Acessando o último elemento
print(cores[-2])  # Acessando o penúltimo elemento
print(cores[-3])  # Acessando o antepenúltimo elemento

print("")

#Append (Adicionando elementos no final da lista)

cores.append("Dourado")  # Adicionando um elemento no final da lista
print(cores)

print("")

#Insert (Adicionando elementos em uma posição específica da lista)

cores.insert(1, "Preto")  # Adicionando um elemento na posição 1
print(cores)

print("")

#remove (Removendo elementos da lista)

cores.remove("Preto")  # Removendo o elemento "Preto" da lista

cores.remove("Dourado")  # Removendo o elemento "Dourado" da lista
print(cores)

print("")

#pop (Removendo elementos da lista pelo índice)

cores.pop(0)  # Removendo o elemento na posição 0
print(cores)

print("")

#sort (Ordenando a lista)

cores.sort()  # Ordenando a lista em ordem alfabética
print(cores)

print("")

#reverse (Invertendo a ordem da lista)

cores.reverse()  # Invertendo a ordem da lista
print(cores)

print("")

#lista de compreensão (Criando uma nova lista a partir de uma existente)

numeros = [1, 2, 3, 4, 5]

quadrados = [x**2 for x in numeros]  # Criando uma nova lista com os quadrados dos números
print(quadrados)