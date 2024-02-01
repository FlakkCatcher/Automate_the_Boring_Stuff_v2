myPets = ["Bagheera", "Binx", "Patch", "Oreo"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("Whose cat is this?  It's not mine!")
else:
    print(name+" is my cat.")