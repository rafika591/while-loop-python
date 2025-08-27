list=[]
while True:
    n=input("Enter the number")
    if n=="exit":
        break
    n=int(n)
    list.append(n*n)
    print(list)
print("Exited the loop")