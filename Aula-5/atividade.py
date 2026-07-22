# ```python
# 1 Imprima uma mensagem de boas-vindas na tela.
# 2 Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
# 3 Imprima o resultado da multiplicação de dois números decimais de sua escolha
# 4 Imprima o resultado da divisão (/)de dois números inteiros de sua escolha.
# 5 Imprima o resultado da subtração de dois números inteiros de sua escolha
# 6 Imprima o resultado da divisão (//)inteira de dois números inteiros de sua escolha.
# 7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha
# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número
# 9 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)
# nome, email, idade, cidade, gradução, estado civil 

print("Seja bem vindo ao Python, Deivis!")

verdadeiro = True 
print(type(verdadeiro))

n1 = 5.5
n2 = 2.5
print(n1*n2)

n3 = 10
n4 = 2
print(n3/n4)

n5 = 20
n6 = 8
print(n5 -n6)

n7 = 10
n8 = 3
print(n7 // n8)

n9 = 2.5
n10 = 1.5
n11 = 3.0
n12 = 2.0
print(n9*n10*n11*n12)

numero = 10
print(numero * 2)

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
idade = input("Digite sua idade:" )
cidade = input("Digite sua cidade:" )
graduacao = input("Digite sua graduacao:" )
estado_civil = input("digite se estado civil:" )

print ("----cadastro----")
print("Nome:",nome)
print("E-mail;",email)
print("Idade:",idade)
print("Cidade:",cidade)
print("Graduação:",graduacao)
print("Estado Civil:",estado_civil)