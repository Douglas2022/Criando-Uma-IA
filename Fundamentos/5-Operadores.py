num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

#Operadores Aritméticos
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mode = num1 % num2
exponent = num1 ** num2
#
#print(sum)
#print(sub)
#print(mult)
#print(div)
#print(exponent)
#print(mode)
#
print(f"A soma é: {sum}")
print(f"A subtração é: {sub}")
print(f"A multiplicação é: {mult}")
print(f"A divisão é: {div}")
print(f"A potência é: {exponent}")
print(f"O resto da divisão é: {mode}")
print(f"O expoente é: {exponent}")

#Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diferent = num1 != num2
bigger_or_equal = num1 >= num2
smaller_or_equal = num1 <= num2

print(f"O primeiro número é maior que o segundo? {bigger}")
print(f"O primeiro número é menor que o segundo? {smaller}")
print(f"Os números são iguais? {equal}")
print(f"Os números são diferentes? {diferent}")
print(f"O primeiro número é maior ou igual ao segundo? {bigger_or_equal}")
print(f"O primeiro número é menor ou igual ao segundo? {smaller_or_equal}")

#Atribuição
num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1

