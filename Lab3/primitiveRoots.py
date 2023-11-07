# check prime
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def checkPrimitiveRoot(num):
    primitive_roots = []
    mod_result = []
    for number in range(2, num):
        is_primitve = True

        for i in range(1, num):
            mod = (number**i) % num
            
            if mod not in mod_result:
                mod_result.append(mod)
            else:
                is_primitve = False
                break

        if is_primitve:
            primitive_roots.append(number)
        
        mod_result.clear()
    
    return primitive_roots


num = int(input("Enter a number to find its primitive root: "))

if(isPrime(num)):
    primitive_roots = checkPrimitiveRoot(num)
    print(primitive_roots)
else:
    print(f"{num} is not a Prime number")