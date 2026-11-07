movieName = "Avengers: Endgame"
#string(iinicio:fim) - indice na posição 0 | indice final - 1

# - Buscar toda string a partitir da primeira letra do indice 0 até a letra na posição
print(movieName[0:]) # Avengers

# 2 - Buscar toda string até a letra na ultima posição. 
print(movieName[:6]) # Avengers: Endgame

# 3 - Buscar toda string da terceira até a última posição.
print(movieName[2:]) # Avengers: Endgame

"""
string[inicio:fim:passo] - indice na posição 0 | indice final - 1 | passo de incremento. Por padrão o passo é 1.
""" 
# 4 - Buscar toda string de 2 em 2 posições, da primeira até a última posição.
print(movieName[::2])
# 5 - Buscar toda string  de numeros impares
print(movieName[1::2])
# 6 - inverte uma string de trás para frente
print(movieName[::-1]) # emadnE :sregnevA   
