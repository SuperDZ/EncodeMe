import math
import random
from typing import Tuple

def generate_prime(bits: int) -> int:
    """Generate a prime number with specified number of bits"""
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keypair(bits: int = 1024) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Generate public and private key pairs"""
    # Generate two prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose public exponent e
    e = 65537  # Commonly used value for e
    
    # Calculate private exponent d
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi
        
    return ((e, n), (d, n))

def encrypt(message: int, public_key: Tuple[int, int]) -> int:
    """Encrypt a message using RSA public key"""
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext: int, private_key: Tuple[int, int]) -> int:
    """Decrypt a message using RSA private key"""
    d, n = private_key
    return pow(ciphertext, d, n)

def text_to_int(text: str) -> int:
    """Convert text to integer"""
    return int.from_bytes(text.encode(), 'big')

def int_to_text(number: int) -> str:
    """Convert integer back to text"""
    return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode()

# Example usage:
if __name__ == "__main__":
    # Generate key pairs
    public_key, private_key = generate_keypair(bits=1024)
    
    # Original message
    message = "Hello, RSA!"
    print(f"Original message: {message}")
    
    # Convert message to integer
    message_int = text_to_int(message)
    
    # Encrypt
    encrypted = encrypt(message_int, public_key)
    print(f"Encrypted: {encrypted}")
    
    # Decrypt
    decrypted_int = decrypt(encrypted, private_key)
    decrypted = int_to_text(decrypted_int)
    print(f"Decrypted message: {decrypted}")
