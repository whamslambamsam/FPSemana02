frase = input("Solicita-me uma frase : ")

frase_escolhida = { }
print(frase)

frase = frase.split()

for palavra in frase:
    caracteres = len(palavra)
    frase_escolhida[palavra] = caracteres

print(frase_escolhida)
