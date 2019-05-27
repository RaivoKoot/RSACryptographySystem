
def generate_keys():
    import sympy

    # chose 2 large prime numbers and compute n
    p = -1
    q = -1
    while(p == q):
        p = sympy.randprime(2**6, 2**9)
        q = sympy.randprime(2**6, 2**9)
    n = q * p


    import random

    # pick an integer bigger than 1 and smaller than (p-1)(q-1)
    e = random.randint(2, (p-1)*(q-1) )

    # find a value d bigger than zero that is
    # congruent to 1 mod (p-1)(q-1) when multiplied by e
    product = (p-1)*(q-1)
    d = -1

    found_d = False
    for i in range(1, 10000000):
        if((i*e) % product == 1):
            d = i
            found_d = True
            break

    if (not found_d):
        print("WARNING")
        print("A correct value for d was not found and the \
resulting computations will not be correct")
        print()

    print("Public Key: (n=" + str(n) + ", e=" + str(e) + ")")
    print("Private Key: " + str(d))

    return {"n": n, "e": e, "d": d}

def encrypt_message(message, n, e):
    encrypted_message = (message**e) % n

    return encrypted_message

def decrypt_message(encrypted_message, d, n):
    decrypted_message = (encrypted_message**d) % n

    return decrypted_message

keys = generate_keys()

original_message = 12345

encrypted_message = encrypt_message(original_message, keys["n"], keys["e"])

decrypted_message = decrypt_message(encrypted_message, keys["d"], keys["n"])

print("Keys " + str(keys))
print("Original Message: " + str(original_message))
print("Encrypted Message: " + str(encrypted_message))
print("Decrypted Message: " + str(decrypted_message))
