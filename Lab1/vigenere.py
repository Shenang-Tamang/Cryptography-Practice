plain_text = input("Enter the plain text: ").replace(" ", "").upper()

alphabets = {chr(65 + i): i for i in range(26)}
rev_alphabets = {val: key for key, val in alphabets.items()}

key = input("Enter the key: ").replace(" ", "").upper()
key = (key + key * int(len(plain_text) / len(key)))[: len(plain_text)]

encrypted_text = decrypted_text = ""

for char, keyChar in zip(plain_text, key):
    encr = (alphabets[char] + alphabets[keyChar]) % 26
    encrypted_text += rev_alphabets[encr]

print("Encrypted Text: ",encrypted_text)

for char, keyChar in zip(encrypted_text, key):
    decr = (alphabets[char] - alphabets[keyChar]) % 26
    decrypted_text += rev_alphabets[decr]

print("Decrypted Text: ",decrypted_text)


# To generate Vigenere table
# maxm = max(key)
# alphabets_ = list(chr(i) for i in range(65, ord(maxm)+1))
# v_table = [alphabets_[i:] + alphabets_[:i] for i in range(len(alphabets_))]

# for row in v_table:
#     print(row)