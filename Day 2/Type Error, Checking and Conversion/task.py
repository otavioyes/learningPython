from xmlrpc.client import boolean

#print(type(123))
#print(type("Hello"))
#print(type(True))
#print(type(10.5))

#PARA QUE EU CONSIGA CONTAR O TOTAL DE UMA STRING SEM TER "ErrorType"
#1. Eu crio uma variavel que recebe uma string
#2. Crio uma segunda variavel que recebe um metodo len() e detro do metodo coloco o nome da 1 variavel

your_name = input("Enter your name: ")
length_name = len(your_name)

print(type("Number of letters in your name is: ")) #str
print(type(length_name)) #int

print("Number of letters in your name is: " + str(length_name))



