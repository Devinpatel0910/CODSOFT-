import random
import string

if __name__=="__main__":
    pass1 = string.ascii_lowercase

    pass2 = string.ascii_uppercase

    pass3 = string.digits

    pass4 = string.punctuation

    passwordlen = int(input("Enter password length\n"))
    password = []
    password.extend(list(pass1))
    password.extend(list(pass2))
    password.extend(list(pass3))
    password.extend(list(pass4))
    random.shuffle(password)
    print("Your password is:")
    print("".join(password[0:passwordlen]))
