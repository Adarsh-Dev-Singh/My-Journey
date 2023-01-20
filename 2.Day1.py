import random
l1 = ['Aadhavi','Aanya','Aarya','Aashvi','Avni','Alia','Amulya','Aniya','Aruhi']
x=0
l2= input("Enter Your name\n")
for i in range(9):
    x=x+1
    v1 = random.choice(l1)
    print(f"{l2} will make out with {v1} on the day  {x}")


