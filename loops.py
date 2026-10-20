#for

for i in range(1, 6):
    print(i)
    
print("Fim do loop for!")

#while

cont = 0

while cont <= 5:
    print(cont)
    cont += 1

print("Fim do loop while!")

#Controle de Loops

#break

cont = 0

while True:
    
    print(cont)
    cont += 1
    
    if cont == 5:
        break

print("Fim do loop com break!")

#continue

for i in range(10):
    
    if i % 2 == 0:
        continue
    print(i)

print("Fim do loop com continue!")

#pass

for i in range(5):
    pass
print("Fim do loop com pass!")