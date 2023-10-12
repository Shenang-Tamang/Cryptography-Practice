# SHA-512 Hashing Algorithm Documentation

The SHA-512 (Secure Hash Algorithm 512) is a cryptographic hash function that produces a fixed-size 512-bit (64-byte) hash value from an input message. This documentation will provide an in-depth explanation of the key components and operations of the SHA-512 algorithm.

## Components

### 1. Additive Constants (K)

SHA-512 uses a set of 80 constant values, known as "additive constants" or "round constants." These constants are used during the compression function and enhance the security of the hash function. A subset of these constants is shown below:


### 2. Initial Hash Values (HASH_VALUE)

The initial hash values are constants that serve as the starting state of the hash function. These values will be updated as each block of the message is processed. Here are the initial hash values:


### 3. SHA-512 Functions

The SHA-512 algorithm relies on several helper functions:

- **Ch(e, f, g)**: The choice function applies a conditional bitwise operation to its arguments.

- **Maj(a, b, c)**: The majority function applies a majority-like bitwise operation to its arguments.

- **rotr(x, n)**: The right-rotate function shifts the bits of a value to the right by `n` positions.

- **summation_a(a)** and **summation_e(e)**: These functions apply specific bitwise operations to the input values `a` and `e`.

- **sigma_0(word)** and **sigma_1(word)**: These functions apply custom bitwise operations to a 64-bit word.

- **addition_modulo_2_64(value)**: This function calculates the modulo operation of a 64-bit value.

### 4. Padding Function (pad_message)

The `pad_message(message)` function is used to pad the input message. It ensures that the message's length is a multiple of 1024 bits (128 bytes) by adding padding bits. The padding includes a '1' bit followed by '0' bits and the original message length.

### 5. Block Division (divide_to_blocks)

The `divide_to_blocks(message)` function divides the padded message into 1024-bit blocks, making it ready for processing.

### 6. Compression Function (round_function)

The core of the SHA-512 algorithm is the compression function. This function processes each 1024-bit block of the message in multiple rounds and updates the internal hash values. Here's a code snippet illustrating the compression function:

```python
W = [0] * 80

def round_function(message):
    a, b, c, d, e, f, g, h = HASH_VALUE

    # Initialization of message schedule W
    for t in range(16):
        W[t] = int.from_bytes(message[t * 8 : (t + 1) * 8], byteorder="big")

    for t in range 16, 80:
        W[t] = sigma_1(W[t - 2] + W[t - 7]) + sigma_0(W[t - 15] + W[t - 16])

    # Main compression loop
    for t in range(80):
        T1 = h + (Ch(e, f, g) + summation_e(e) + K[t] + W[t])
        T2 = summation_a(a) + Maj(a, b, c)

        # Update hash values
        h = g
        g = f
        f = e
        e = addition_modulo_2_64(d + T1)
        d = c
        c = b
        b = a
        a = addition_modulo_2_64(T1 + T2)

    # Update intermediate hash values
    HASH_VALUE[0] = addition_modulo_2_64(HASH_VALUE[0] + a)
    HASH_VALUE[1] = addition_modulo_2_64(HASH_VALUE[1] + b)
    # ... (more values) ...
    HASH_VALUE[7] = addition_modulo_2_64(HASH_VALUE[7] + h)
```

## Usage

To compute the SHA-512 hash of a message, you can use the provided functions as follows:

```python
message = input("Enter a message: ").encode("utf-8")
padded_message = pad_message(message)
blocks = divide_to_blocks(padded_message)

for block in blocks:
    round_function(block)

final_hash = "".join(format(h, "016x") for h in HASH_VALUE)
print(final_hash)
```

This code takes an input message, processes it using the SHA-512 algorithm, and prints the resulting hash value.
