import time

start=time.time()
def sieve_of_eratosthenes(n):
    is_prime=[True]*(n-1)
    p=2
    while True:
        multiplier=2
        multiple=p*multiplier
        while multiple<=n:
            is_prime[multiple-2]=False
            multiplier+=1
            multiple=p*multiplier
        for i,prime in enumerate(is_prime):
            if prime and i+2>p:
                p=i+2
                break
        else:
            return is_prime
def primefactorization(list,n):
    temp_list=[]
    product=1
    for i,prime in enumerate(list):
        if (product >= n):
            break
        modulus=n
        if n % prime == 0:
            temp_list.append(prime)
            product=product*prime
            modulus=modulus/prime

        while(modulus%prime==0):
            temp_list.append(prime)
            product = product * prime
            modulus = modulus / prime
    return temp_list

num1=int(input("enter num1"))
num2=int(input("enter num2"))
prime_list1=[]
prime_list2=[]

prime_list1=sieve_of_eratosthenes(num1)
prime_list2=sieve_of_eratosthenes(num2)

actual_prime_list1=[]
actual_prime_list2=[]
#prime_list=list(filter((False).__ne__,prime_list))

for i,prime in enumerate(prime_list1):
    if prime:
        actual_prime_list1.append(i+2)

for i,prime in enumerate(prime_list2):
    if prime:
        actual_prime_list2.append(i+2)
print("first prime numbers:")
print(actual_prime_list1)
print("second prime numbers:")
print(actual_prime_list2)

fact_list1=primefactorization(actual_prime_list1,num1)
fact_list2=primefactorization(actual_prime_list2,num2)
print("factorization of list1")
print(fact_list1)
print("factorization of list2")
print(fact_list2)
gcd=[]

if len(fact_list1)<len(fact_list2):
    for element in fact_list1:
        if element in fact_list2:
            gcd.append(element)
else:
    for element in fact_list2:
        if element in fact_list1:
            gcd.append(element)

print("common prime factors",gcd)
pro=1
for i in gcd:
    pro=pro*i
print("gcd is"+str(pro))
end=time.time()
print("--- %s seconds ---" % (end - start))


















