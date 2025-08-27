# 5. Menu-Driven Calculator 
# Question: 
# Write a program that continuously shows a menu: 
# 1. Add 
# 2. Subtract 
# 3. Multiply 
# 4. Divide 
# 5. Exit 
while True:
    print("\nMenu\n1.Add\n2.Suntract\n3.Multiply\n4.Divide\n5.Exit\n")
    choice=int(input("Enter your choice:"))
    if choice ==5:
        print("Exiting program...")
        break
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        if b!=0:
            print(a/b)
        else:
            print("Division by zero is not possible")