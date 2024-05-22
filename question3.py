#write a program to find the factorial of a nummber
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    fact=n*fact(n-1)
    return fact
n=int(input(Enter the number:))
fact(n)
