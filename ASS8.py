def accept(C,Str):
    n=int(input("Enter no. total of students playing %s :"%Str))
    for i in range(n):
        m=int(input("Enter name of student %d playing %s :"%((i+1),Str)))
        C.append(m)
    
def display(C,Str):
    n=len(C)
    if(n==0):
        print("\nGroup of students playing %s = {}"%Str)
    else:
        print("\nGroup of students playing %s = {"%Str)
        for i in range(n-1):
            print("%s,"%C[i])
        print("%s }"%C[n-1])

def search(C,x):
    n=len(C)
    for i in range(n):
        if(C[i]==x):
            return (1)
        return (0)

def intersection(C,B,F):
    for i in range(len(C)):
        flag=search(B,C[i])
        if(flag==1):
            F.append(C[i])

def difference(C,B,F):
    for i in range(len(C)):
        flag=search(B,C[i])
        if(flag==0):
            F.append(C[i])

def union(C,B,F):
    for i in range(len(C)):
        F.append(C[i])
    for i in range (len(B)):
        flag=search(C,B[i])
        if(flag==0):
            F.append(B)

def main():
    Group_C=[]
    Group_B=[]
    Group_F=[]

    while True:
        print("\t 1.Accept.")
        print("\t 2.plays both C and B.")
        print("\t 3.plays either C or B but not F.")
        print("\t 4.plays nethier C nor B.")
        print("\t 5.plays C and F but not B.")
        print("\t 6.Exit.")

        ch=int (input("enter your choice :"))
        Group_R=[]

        if(ch==6):
            print("End of program ")
            break
    
        elif(ch==1):
            accept(Group_C,"Cricket")
            display(Group_C,"Cricket")
            accept(Group_B,"Badminton")
            display(Group_B,"Badminton")
            accept(Group_F,"Football")
            display(Group_F,"Football")

        elif(ch==2):
            display(Group_C,"Cricket")
            display(Group_B,"Badminton")
            intersection(Group_C,Group_B,Group_R)
            display(Group_R,"both Cricket and Badminton.")

        elif(ch==3):
            Group_R1=[]
            Group_R2=[]
            display(Group_C,"Cricket")
            display(Group_B,"Badminton")
            display(Group_F,"Football")
            union(Group_C,Group_B,Group_R1)
            intersection(Group_C,Group_B,Group_R2)
            difference(Group_R1,Group_R2,Group_R)

        elif(ch==4):
            Group_R3=[]
            Group_R4=[]
            display(Group_C,"Cricket")
            display(Group_B,"Badminton")
            display(Group_F,"Football")
            union(Group_B,Group_C,Group_R3)
            difference(Group_F,Group_R3,Group_R4)
            display(Group_R,"neither Cricket nor badminton")
            print("Number of students who play neither cricket nor badmiton =%s"%len(Group_R))

        elif(ch==5):
            Group_R5=[]
            display(Group_C,"Cricket")
            display(Group_B,"Badminton")
            display(Group_F,"Football")
            intersection(Group_C,Group_F,Group_R5)
            difference(Group_B,Group_R5,Group_R)
            display(Group_R,"plays C and F but not B.")
            print("Number of student who play cricket and football but not badminton .=%s"%len(Group_R))

        else:
            print("Wrong Choice Entered !! Try again ")

main()
quit()

