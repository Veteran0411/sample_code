# a={1:110,2:20,3:30}
# b=sorted(a.items(),key=lambda x:x[1])
# print(b)

a=[1,2,3,4]
b=list(map(lambda v:v+10,a))
print(b)