# fibonacci using recursive functione
# def fibonacci(n,memo={}):
#     if n in memo:
#         return memo[n]
#     if n<=1:
#         return n
#     memo[n]=fibonacci(n-1)+fibonacci(n-2)
#     return memo[n]

def fibo(n):
    if n<=1:
        return n
    a=[0]*(n+1)
    a[0]=1
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-2]+a[i-1]
    print(a)
    return a[n]
    
    
# def fibo(n):
#     if n<=1:
#         return n
#     a=[0]*n
#     a[0]=1
#     a[1]=1
#     for i in range(2,n):
#         a[i]=a[i-2]+a[i-1]
#     print(a)
#     return a[n-1]
print(fibo(7))

# 1,1,2,3,5,8,13