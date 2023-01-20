def sundarladki(k):
    x=1
    for i in range(k):
        x = x * (i + 1)
    return x
print("Enter the number of which you want factorial :\n")
sabse_sundar_ladki = int(input())
print(f"The required factorial is {sundarladki(sabse_sundar_ladki)}")