# 1. Write a Python program to calculate the sum of the first n natural 
# numbers using a while loop. 
i=1
sum=0
n=int(input("Enter the range"))
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)