import random as r

def calculateKey(y, x, q):
    return (y**x) % q

q = int(input("Enter a prime number (q): "))

alpha = int(input("Enter a primitive root of q (alpha): "))

xA = r.randint(1, q)
xB = r.randint(1, q)

yA = (alpha**xA) % q
yB = (alpha**xB) % q

kA = calculateKey(yB, xA, q)
kB = calculateKey(yA, xB, q)

print("Public key of A (kA): ", kA)
print("Public key of B (kB): ", kB)