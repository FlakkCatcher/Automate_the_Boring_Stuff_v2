def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid Argument")

print(spam(2))
print(spam(12))
print(spam(0))                  #The error is in this line, but since the try block only references the function, it will not stop the code execution
print(spam(1))                  #This line will be run in the code execution
print()
#Any errors in the TRY block will be caught, so if you can separate them out, you can minimize errors
print()
def eggs(division):
    return 42 / division

try:
    print(eggs(2))
    print(eggs(12))
    print(eggs(0))              #The error will be caught here, so the code execution will stop at this line
    print(eggs(1))              #This line will not be executed
except ZeroDivisionError:
    print("Error: Invalid Argument")