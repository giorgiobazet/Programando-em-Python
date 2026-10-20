# 1. Criar uma classe própria para o erro
class MeuErroPersonalizado(Exception):
    pass

# 2. Definir a 'condicao' como parâmetro da função
def funcao(condicao):
    if condicao:
        # 3. Levantar a exceção personalizada em vez da genérica
        raise MeuErroPersonalizado("Descrição do erro")

try:
    # Passamos 'True' para testar a ativação do erro
    funcao(True) 
except MeuErroPersonalizado as e:
    print(f"Erro: {str(e)}")