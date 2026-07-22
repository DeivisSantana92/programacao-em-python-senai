n1  =  float(input('Nº'))
op =  input('Digite a operação: ')
n2  =  float(input('Nº'))
resultado =  (op == '+' and (n1 +  n2)) or (op == '-' and n1 - n2) or (op == '*' and n1 * n2) or (op == '/' and n1 /n2)


print(resultado)
idade  =  int(input('Idade: '))
carta_motorista = input('Possui carta: ')


resultado = (idade >= 18 and carta_motorista == 'sim' and ('Pode dirigir...')) or ('Não pode ...')


print(resultado)

n1 = float(input("10: "))
n2 = float(input("8: "))
n3 = float(input("3 :"))

media = (n1 + n2 + n3) / 3
print ( f"A media das notas é: {media: .2f}")
if media >=7:
    print("Passou de ano!")
else:
    print("Não passou de ano!")