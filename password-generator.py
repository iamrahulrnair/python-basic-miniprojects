import random


def main():
    
    _length=int(input("Length of the password?: "))
    password=[]
    for i in range(_length):
        password.append(chr(random.randint(33,122)))
    
    print("".join(password))


main()