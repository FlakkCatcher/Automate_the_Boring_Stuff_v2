def collatz(x):
    while x > 1:
        if x % 2 == 0:
            x = x // 2
            print(x)
        else:
            x = 3*x + 1
            print(x)
            
try:
    number = int(input("Enter a number: "))
    collatz(number)
except ValueError:
    print("You can only enter integers to start a Collatz Sequence.")