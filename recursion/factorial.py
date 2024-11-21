def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def factorial1(n):
    fact=1
    for i in range(n,1,-1):
        fact*=i
    print(fact)
n=5
print(f"factorial of {n} is {factorial1(n)}")