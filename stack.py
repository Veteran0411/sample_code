stack=[]
def push():
    a=input("enter elements of stack: ").split()
    for i in a:
        stack.append(int(i))
    print(stack)

def pop():
    n=int(input("enter number of elements to pop: "))
    for i in range(n):
        stack.pop()
    print(stack)
push()
pop()