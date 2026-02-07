# vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Recebendo os números do usuário
texto = input("Digite uma string: ")
repeticoes = int(input("Digite um número inteiro: "))

# Repetindo a string o número de vezes informado
resultado = (texto + ' ') * repeticoes

# Exibindo o resultado
print("String repetida:", resultado)
