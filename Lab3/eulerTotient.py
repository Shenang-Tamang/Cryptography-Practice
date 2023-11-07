def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
    
n = int(input("Enter a number: "))
count = 0

for i in range(n):
    gcdres = gcd(i, n)
    if gcdres == 1:
        count += 1

print(f"φ({n}) is {count}")