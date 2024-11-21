# nh fibonacci number
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def printFibonacci(n):
    fib=[0,1]
    if n==0:
        return
    elif n==1:
        print(0)
    elif n==2:
        print(0,1)
    for i in range(2,n+1):
        nextFib=fib[-1]+fib[-2]
        fib.append(nextFib)
    return fib

if __name__=="__main__":
    n=int(input("enter the number of fibonacci numbers: "))
    print("fibonacci sequence:==")
    print(*printFibonacci(n))
    