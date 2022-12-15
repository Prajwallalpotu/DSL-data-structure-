list=[]
n=int(input("Entre no. of elements in list :"))
for i in range(n):
    a=int(input("enter elements in list :"))
    list.append(a)
print(list)

def partition(list,p,q):
    x=list[p]
    i=p
    for j in range(i+1,q+1):
        if(list[j]<=x):
            i+=1
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
    temp1=list[i]
    list[i]=list[p]
    list[p]=temp1
    return i

def quicksort(list,p,q):
    if(p<q):

        i=partition(list,p,q)
        quicksort(list,i+1,q)
        quicksort(list,p,i-1)

quicksort(list,0,n-1)

print(list)



