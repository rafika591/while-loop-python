# 2. Write a Python program that takes an integer as input and prints its 
# digits in reverse order using a while loop. 
sum=0
n=int(input("Enter the digit"))
while(n>0):
    rem=n%10
    sum=sum*10+rem 
    n=n//10
print(sum)