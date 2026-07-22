# 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

# 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

# 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

# 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

# 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

numero = int(input(10))
quadrado = numero **2
print(f"O quadrado de {numero}é{quadrado}")

primeiro_nome = "Deivis"
sobrenome = "Santana"
nome_completo = primeiro_nome + " "+sobrenome
print (nome_completo)

n1 = int(input("10"))
n2 = int(input("20"))
resultado = str(n1) + str(n2)
print(resultado)

palavra = "Python"
numero =3 
resultado = palavra + str(numero)
print(resultado)

Frase = "Eu estou aprendendo"
palavra = input("Digite uma palavra:")
resultado = Frase + palavra
print(resultado)