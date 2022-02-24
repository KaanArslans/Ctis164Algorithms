def euclid(m,n):
    if n==0:
        return m
    else:
        return euclid(n,m%n) #recursive function for euclid algorithm


num1=int(input("enter first number for gcd"))
num2=int(input("enter second number for gcd"))
result=euclid(num1,num2)
print("gcd from euclid is",result)









