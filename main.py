ls=[4,35,65,4,756,232,76,67,345,32,56]
flag=0
i=0
while True:
        if i>=(len(ls)-1): 
            i=0
            if flag==0:
                break
            else:
                flag=0
        if ls[i]>ls[i+1]:
            flag=1
            ls[i]+=ls[i+1]
            ls[i+1]=ls[i]-ls[i+1]
            ls[i]-=ls[i+1]
        i+=1
print(ls)