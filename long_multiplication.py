def karatsuba(x, y):
    
    if x < 10 or y < 10:
        return x * y

    
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

   
    return (ac * 10**(2 * m)) + (ad_plus_bc * 10**m) + bd

def long_multiplication(x, y):
    return karatsuba(x, y)

try:
    x = int(input("Enter the first number (x): "))
    y = int(input("Enter the second number (y): "))
    result = long_multiplication(x, y)
    print(f"Multiplication of {x} and {y} is: {result}")
except ValueError:
    print("Please enter valid integers.")
