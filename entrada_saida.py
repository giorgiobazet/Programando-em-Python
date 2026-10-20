nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))


print("Olá, " + nome + "!")
print("Você tem " + str(idade) + " anos.")

idade2 = int(input("Insira sua idade: "))


if idade2 >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

nome2 = "Giorgio"
idade3 = 19

print(f"Olá, meu nome é {nome2} e eu tenho {idade3} anos.")