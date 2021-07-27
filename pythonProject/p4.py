#Wap which takes a number from  and find out the factorial of given number
facto = int(input("Enter any number:"))
n=facto-1
while n>0:
    facto = facto*n
    n=n-1
print(facto)
