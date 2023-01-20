import random
l1 = []
n = int(input("Enter the number of Girls you want to go out with\n"))
print("Enter their names")
for i  in range(0,n):
    budha = input()
    l1.append(budha)
v1=random.choice(l1)
print(f"The one which is made for you is {v1}")