import random

def encryption(alpha, kpub, p,PlainText):
    e = random.randint(1, p-1)  #private key
    C1 = (alpha ** e) % p
    
    C2 = (PlainText * (kpub ** e)) % p
    
    return C1, C2

def keyGeneration(): 
    p =  int(input("Enter a prime number: "))  #prime number
    alpha =  int(input(f"Enter a primitive root of {p}: "))  #primitive root
    d = random.randint(1, p-1)  #private key
    kpub = (alpha ** d) % p
    return alpha, kpub, d,  p

def decryption(d, p, C1, C2):
    for i in range(p):
        if((pow(C1, d) * i) % p == 1):
            C1inv = i
    P = C2 * C1inv % p
    return P

if __name__ == "__main__":
    alpha, kpub, d , p = keyGeneration()
    PlainText = int(input(f"Enter a plain text under {p}: "))

    C1, C2= encryption(alpha, kpub, p, PlainText)
    print(f"Cipher: {C1}, {C2}")
    P = decryption(d, p, C1, C2)
    print(f"Plain text: {P}")