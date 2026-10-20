#Definição e chamada de funções

def saudacao():
    print("Olá! Bem-vindo ao nosso programa.")
    
saudacao()

#Parâmetros e argumentos

def saudacao2(nome):
    print(f"Olá, {nome}!")
    
saudacao2("Giorgio")

#Valores de retorno


def multiplicacao(a, b):
    return a * b

resultado = multiplicacao(5, 3)
print(f"O resultado da multiplicação é: {resultado}")

#Funções anônimas (lambda)

quadrado = lambda x: x ** 2
resultado = quadrado(4)
print(f"O resultado do quadrado é: {resultado}")

#Escopo das variáveis (local x global)

variavel_global = "Sou uma variável global"

def funcao():
    variavel_local = "Sou uma variável local"
    print(variavel_local)


def funcao2():
    print(variavel_global) 

funcao()
funcao2()
print(variavel_global) 

#Funções com número variável de argumentos
 
def  soma_varivael(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = soma_varivael(1, 2, 3, 4, 5)
print(f"O resultado da soma é: {resultado}")