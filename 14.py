n=int(input("enter a number : "))

def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return "not prime number"
    return "prime number"

print(prime(n))