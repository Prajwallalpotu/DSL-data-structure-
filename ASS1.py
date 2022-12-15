a=[]
n=int(input("enter a number of students in class :"))
for i in range(n):
    d=int(input("enter marks or absent(-1) of student in test :"))
    a.append(d)

def search():
    flag=0
    key=int(input("enter key number : "))
    for i in range(n):
        if(a[i]==key):
            flag=1
            break
    if(flag==0):
        print("absent.")
    if(flag==1):
        print("present.")

def avg():
    count=0
    sum=0
    for i in range(n):
        if(a[i]!=-1):
            sum=sum+a[i]
            count=count+1
            
    print("AVERAGE OF MARKS :",sum/count)

def max():
    max=0
    for i in range(n):
        if(a[i]>max):
            max=a[i]
    print("maximum marks is :",max)

def abs():
    flag=0
    for i in range(n):
        if(a[i]==-1):
            flag=flag+1
    print("OUT OF", n ,"NO. OF STUDENTS ",flag,"ARE ABSENT.")

def fre():
    b=[]
    max1=0
    for i in range(101):
        b.append(0)
    for i in range(n):
        for j in range(101):
            if(a[i]==j):
                b[j]+=1
    for i in range(101):
        if(b[i]>max1):
            max1=b[i]
            t=i
    print("highest frequency is :",t)

def min():
    min=max
    for i in range(n):
        if(a[i]!=-1 and a[i]<min):
            min=a[i]
    print("minimum marks is :",min)


def main():
    print(a)
    while True:
        print("\t")
        print("1.to search a marks of student.")
        print("2.Avg of marks.")
        print("3.to find maximum marks.")
        print("4.no. of absent students is ")
        print("5.to find highest frequency.")
        print("6.EXIT\n")    
        ch=int(input("Enter choice :"))
        if(ch==1):
            search()
        elif(ch==2):
            avg()
        elif(ch==3):
            max()
        elif(ch==4):
            abs()
        elif(ch==5):
            fre()
        elif(ch==6):
            break;
        else:
            print("Invalid Choice ")
    # avg()
    # min()
    # max()
    # abs()
    # fre()

main()
