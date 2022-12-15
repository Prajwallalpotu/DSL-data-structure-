arr=[]
n=int(input("Enter no. of elements in array :"))
for i in range(n):
    a=int(input("Enter values in array :"))
    arr.append(a)
print(arr)

def selection_sort():
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print(arr)

def bubble_sort():
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)
    print("top 5 percentages are :")
    for i in range(-1,-6,-1):
        print(arr[i])
def main():
    while True:
        print("1.selection sort .")
        print("2.bubble sort .")
        print("3.Exit.")
        print("Enter choice :")
        ch=int(input())
        if(ch==3):
            break
        elif(ch==1):
            selection_sort()
        elif(ch==2):
            bubble_sort()
        else:
            print("INVALIDE CHOICE ")

main()
