import random
# l=[1,2,1,5,3,4,5]
# l=list(str(random.randint(1,10)))
l=[]
n=int(input("how many no. do  you want to store in list: "))
for i in range(n):
    l.append(random.randint(1,100))
print(l)

for i in range(len(l)):
    
    if l[i]>=l[i+1]:
        print(l[i])
    
    if i==(n-2):
        break
# else:
#     print("None")
    # else:
    # #     print(l[i+1])
