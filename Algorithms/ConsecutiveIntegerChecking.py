#consecutive integer checking algorithm

def gcd(m,n):

    minimum=min(m,n)
    while(minimum>1):
        if (m % minimum == 0 and n % minimum == 0):
            return minimum
        minimum-=1
    return 1

num1=int(input("enter first number"))
num2=int(input("enter second number"))
result=gcd(num1,num2)
print("gcd is",result)








