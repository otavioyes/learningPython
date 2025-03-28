import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#preciso criar uma variavel que armazena o random.choice e dentro dele vai minha lista com os nomes
names = random.choice(friends)

print(f"The {names} pay the bill")
