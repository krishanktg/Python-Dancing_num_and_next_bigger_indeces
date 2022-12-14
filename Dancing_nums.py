n=input()
for i in range(int(n)+1):
    if len(str(i))==1:
        print(i,end=",")
    else:
        j=0
        # while j < len(str(i)):
        for j in range(len(str(i))):
            if int(str(i)[len(str(i))-j]) - int(str(len(i))[len(str(i))-j-1])==1 or int(str(i)[len(str(i))-j-1]) - int(str(i)[len(str(i))-j])==1:
                print(i,end=",")
            if j==1:
                break 
            # j+=1