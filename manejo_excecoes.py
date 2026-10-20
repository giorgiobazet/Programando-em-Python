#try

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
    
#except

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
    
#finally

arquivo = None
try:
    arquivo = open("arquivo.txt", "r")
    # Realizar operações
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    if arquivo is not None:
        arquivo.close()
