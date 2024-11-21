a = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

roman=input("enter the roman number: ")
total=a[roman[-1]]
for i in range(len(roman)-1,0,-1):
    if a[roman[i-1]] < a[roman[i]]:
        total=total-(a[roman[i-1]])
        continue
    total=total+a[roman[i-1]]
print(total)
