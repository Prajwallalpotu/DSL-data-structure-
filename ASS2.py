mat1=[]
mat2=[]

r1=int(input("Enter rows in matrix 1 : "))
c1=int(input("Enter columns in matrix 1 : "))
print("\n")
r2=int(input("Enter rows in matrix 2 : "))
c2=int(input("Enter columns in matrix 2 : "))
print("\n")

def accept(mat,r,c):
    for i in range(r):
        d=[]
        for j in range(c):
            e=int(input("Enter the Elements : "))
            d.append(e)
        mat.append(d)


def display(mat,r):

    for i in range(r):
        print(mat[i])

def add(mat1,mat2,r,c):
    add=[]
    for i in range(r):
        s=[]
        for j in range(c):
            q=mat1[i][j]+mat2[i][j]
            s.append(q)
        add.append(s)
    print("MAT1 + MAT2 = ")

    for i in range(r):
        print(add[i])


def sub(mat1,mat2,r,c):
    sub=[]
    for i in range(r):
        h=[]
        for j in range(c):
            k=mat1[i][j]-mat2[i][j]
            h.append(k)
        sub.append(h)
    print("MAT1 - MAT2 = ")

    for i in range(r):
        print(sub[i])

def mul(mat1,mat2,r1,c1,c2):
    mul=[]
    for i in range(r1):
        o=[]
        for j in range(c2):
            o.append(0)
        mul.append(o)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                mul[i][j]+=mat1[i][k]*mat2[k][j]
    
    print("MATRIX 1 x MATRIX 2 = ")
    for i in range(c1):
        print(mul[i])

def transpose(mat,r,c):
    trans=[]
    for i in range(r):
        l=[]
        for j in range(c):
            l.append(mat[j][i])
        trans.append(l)
    print("transpose of matrix :")
    for i in range(r):
        print(trans[i])

def main():
    accept(mat1,r1,c1)
    display(mat1,r1)
    accept(mat2,r2,c2)
    display(mat2,r2)

    while True:

        print("1.Enter addition. ")
        print("2.Enter subtraction. ")
        print("3.Enter multiplication. ")
        print("4.Enter transpose. ")
        print("5.Exit.")
        print("##### ENTER CHOICE #####")
        ch=int(input())
        if(ch==5):
            exit
        elif(ch==1):
            add(mat1,mat2,r1,c1)
        elif(ch==2):
            sub(mat1,mat2,r1,c1)
        elif(ch==3):
            mul(mat1,mat2,r1,c1,c2)
        elif(ch==4):
            transpose(mat1,r1,c1)
        else:
            print("INVALID CHOICE !!!")

main()