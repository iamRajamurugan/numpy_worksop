#write a program to find the sum of digits of a given number'
n=input("Enter a number:")
l=list(n)
sum=0
for s in n:
  sum=sum+int(s)
print(sum)
