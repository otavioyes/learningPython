# password_pass = input("New password: ")
#
# def password():
#     while True:
#         new_password = input("Enter your password: ")
#         if password_pass == new_password:
#             print("Welcome")
#         else:
#             print("Acess invalid")
#
# password()

def while_check():
    total = 0
    while total <= 10000:
        print(f"TOTAL = {total}")
        if total == 10000:
            print(f"o total é : {total}")
        else:
            print()
        total += (1 * 3.1415) / 2



while_check()