palavra1 = input("Solicita-me uma palavra: ")
palavra2 = input("Solicita-me outra: ")

print(palavra1)
print(palavra2)

palavras = ()

# Para fazer um set, utiliza-se o comando "set()"
palavra1 = set(palavra1)
palavra2 = set(palavra2)

intersecao = palavra1.intersection(palavra2)

resultado = "".join(list(intersecao))

print(resultado)
