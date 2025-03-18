# convertendo a entrada para inteiro
# calcula o resto da divisão por 2
# SE o resto for 0 imprime isso
# caso contrario, mostro o resto

number = float(input("Enter a number: "))

remainder = number % 2

if remainder == 0:
    print(f"The rest of division is 0")
else:
    print(f"The rest of division is: {remainder}")