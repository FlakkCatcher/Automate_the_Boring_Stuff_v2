def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs)
    
spam()
#This program should print out the following: 0, 99
#This is because the program calls spam() which has a local variable for eggs set to 99, then it calls bacon() which has the same local variable set to 0
#The bacon() function contains a print(eggs), which calls the 0 version, then the spam() function's print(eggs) calls its own 99 version