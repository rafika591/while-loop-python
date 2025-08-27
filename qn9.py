# 3. Write a Python program to find the factorial of a number using a while 
# loop. 
fact=1
n=int(input("Enter the number:"))
while(n>0):
    fact=fact*n
    n=n-1
print(fact)