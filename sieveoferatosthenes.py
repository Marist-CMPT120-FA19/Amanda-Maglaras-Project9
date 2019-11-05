#Amanda Maglaras
#amanda.maglaras1@marist.edu
#This project allows us to find prime numbers

def prime(n):
    a = []
    b = []
    for i in range(2,n+1):
        if i not in a:
            b.append(i)
            for j in range(i*i,n+1,i):
                a.append(j)
    return b
primenumber = int(input("Enter a number: "))
print(prime(primenumber))

prime
