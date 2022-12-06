arr=[]
n=int(input("enter length"))
for i in range(0,n):
    a=int(input())
    arr.append(a)
max=arr[n-1]
print(max)
for i in range(n-2,-1,-1):
    if(max<arr[i]):
        max=arr[i]
        print(max)
