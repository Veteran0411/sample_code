# dp
# def factorial(n,memo={}):
#     if n in memo:
#         return memo[n]
#     if n==1 or n==0:
#         return 1
#     memo[n]=n*factorial(n-1,memo)
#     return memo[n]

def factorial(n):
    result=1
    for i in range(n,1,-1):
        result*=i
    return result
print(factorial(5))