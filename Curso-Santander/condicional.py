#if

idade = 18

tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Você pode dirigir!")

#if-else

idade = 16
maior_idade = idade >= 18

if maior_idade:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
    
#if-elif-else

nota = 7.5

if nota >= 9:
    print("Parabéns! Você tirou uma nota excelente!")
elif nota >= 7:
    print("Você tirou uma boa nota!")
else:
    print("Você precisa estudar mais!")