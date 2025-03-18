print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10% 12% 15% "))
people = int(input("How many people to split the bill? "))
# 1.preciso dividir primeiro o total pago por 100
divide_by_one_hundred = tip / 100
# 2.Depois pegar o resultado e multiplicar pelo valor que foi pago
divided_value = bill * tip
# 3. Agora pego o valor total que deu com uma varivel que recebe o total da conta e + o dividy_by_one_hubdread
total_divided_by_person = bill + divide_by_one_hundred
# 4.crio uma variavel que recebe o total da conta divido pela quantidade de pessoas
total_per_person = total_divided_by_person / people
# 5.agora eu crio uma varivel que é o montante e arredonda para duas casas decimais
final_amount = round(total_per_person, 2)
# 6. Imprimo suando f"oque quero imprimir" e coloco {} para juntar no mesmo print oque eu quero
print(f"Each person should pay: ${final_amount}")



