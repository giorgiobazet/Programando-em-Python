arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

arquivo = open("dados2.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)