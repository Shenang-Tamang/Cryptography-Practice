import numpy as np

# Functions

def cipherDecipher(text, key):
    alphabets = [ord(char) - ord('A') for char in text]
    n = len(key)
    num_of_padding = (len(alphabets) % n)
    alphabets += [1] * num_of_padding

    text=''
    for i in range(0, len(alphabets), n):
        block = alphabets[i : i + n]
        product = np.dot(key, block) % 26
        text += "".join(chr(65 + i) for i in product)

    return text, num_of_padding

def inverseOfKey(key):
    # Determinant
    determinant = int(np.ceil(np.linalg.det(key) % 26))

    #Finding 1/det 
    for i in range(26):
        if (determinant * i) % 26 == 1:
            determinant = i
            break

    # Adjoint
    adjKey = np.linalg.inv(key) * np.linalg.det(key)

    for index in range(len(adjKey)):
        for col_index in range(len(adjKey)):
            if adjKey[index][col_index] < 0:
                adjKey[index][col_index] = np.ceil(adjKey[index][col_index] % 26)

    adjKey = adjKey.astype(int)

    return ((determinant * adjKey) % 26)


#Input Data

plain_text = input("Enter the plain text: ").replace(" ", "").upper()

key = np.array([[5, 8], [17, 3]])

# Encryption
cipher_text, paddings = cipherDecipher(plain_text, key)
print("Cipher Text: " + cipher_text)

#inverse of the key.
inv_key = inverseOfKey(key)

# Decryption
decipher_text, temp = cipherDecipher(cipher_text, inv_key)
print("Deciphered Text: " + decipher_text[:(len(cipher_text)-paddings)]) #omiting the padded numbers