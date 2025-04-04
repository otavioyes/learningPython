password_pass = input("New password: ")

def password():
    while True:
        new_password = input("Enter your password: ")
        if password_pass == new_password:
            print("Welcome")
        else:
            print("Acess invalid")

password()