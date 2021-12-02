def collatz(number):
    if number==1:
        print(number)
        return
    if number%2==0:
        print(number)
        collatz(number//2)
    else:
        print(number)
        collatz((3*number)+1)
collatz(26)