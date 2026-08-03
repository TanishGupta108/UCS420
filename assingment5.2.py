n=int(input("Enter number: "))
sum=0
for i in range(1, n+1):
    if i%7==0 and i%9==0:
        sum=sum+i
print("Sum of numbers divisible by 7 and 9 is: ", sum)