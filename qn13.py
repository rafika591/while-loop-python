n=int(input("Enter the number:"))
while(n!=1):
    if n%2==0:
        print(n,end="->")
        n=n//2
    else:
        print(n,end="->" )
        n=n*3+1
print(n)