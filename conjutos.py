#criação e acesso

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#união

uniao = conjunto1 | conjunto2
print(uniao)
print("")

#interseção

intersecao = conjunto1 & conjunto2
print(intersecao)
print("")

#diferença

diferenca = conjunto1 - conjunto2
print(diferenca)
print("")

#diferença simétrica

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)
print("")

#métodos de conjuntos

frutas = {"maçã", "banana", "laranja"}

#add 

frutas.add("uva")  # Adicionando um elemento ao conjunto
print(frutas)

#remove

frutas.remove("banana")  # Removendo um elemento do conjunto
print(frutas)

#discard

frutas.discard("laranja")  # Removendo um elemento do conjunto (não gera erro se o elemento não existir)
print(frutas)

#clear

frutas.clear()  # Limpando todos os elementos do conjunto
print(frutas)