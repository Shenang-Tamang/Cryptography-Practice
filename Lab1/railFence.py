def rail_fence_encrypt(message, rail_count):
    encrypted_message = [''] * rail_count
    direction = -1  # Direction for zigzag pattern: -1 for going up, 1 for going down
    row = 0

    for char in message:
        encrypted_message[row] += char
        if row == 0 or row == rail_count - 1:
            direction *= -1  # Change direction at the edges of the zigzag pattern
        row += direction

    return ''.join(encrypted_message)

def rail_fence_decrypt(encrypted_message, rail_count):
    message_length = len(encrypted_message)
    decrypted_message = [''] * message_length
    direction = -1  # Direction for zigzag pattern: -1 for going up, 1 for going down
    row = 0

    # Generate the rail order to reconstruct the original message
    rail_order = sorted(range(message_length), key=lambda x: (x % (2 * rail_count - 2), x))

    for i in range(message_length):
        decrypted_message[rail_order[i]] = encrypted_message[i]
        if row == 0 or row == rail_count - 1:
            direction *= -1  # Change direction at the edges of the zigzag pattern
        row += direction

    return ''.join(decrypted_message)

if __name__ == "__main__":
    # Get the message from the user
    message = input("Enter the message to encrypt: ")

    # Define the number of rails for encryption and decryption
    rail_count = 3

    # Perform encryption
    encrypted_message = rail_fence_encrypt(message, rail_count)
    print(f"Encrypted message: {encrypted_message}")

    # Perform decryption using the same encrypted text
    decrypted_message = rail_fence_decrypt(encrypted_message, rail_count)
    print(f"Decrypted message: {decrypted_message}")
