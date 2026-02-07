# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Recebendo a palavra do usuário
palavra = input("Digite uma palavra: ")

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se a palavra é um palíndromo
if palavra == palavra_invertida:
    resultado = "é um palíndromo"
else:
    resultado = "não é um palíndromo"   

# Exibindo o resultado
print("A palavra", palavra, resultado)
