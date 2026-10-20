pessoa = {"nome": "Giorgio", "idade": 19, "cidade": "Queimados"}

print(pessoa["nome"])  # Acessando o valor associado à chave "nome"
print(pessoa["idade"])  # Acessando o valor associado à chave "idade"
print(pessoa["cidade"])  # Acessando o valor associado à chave "cidade"

#keys

print(pessoa.keys())
print("")

#values

print(pessoa.values())
print("")

#items 

print(pessoa.items())
print("")

#update

pessoa.update({"profissao": "Programador"})
print(pessoa)