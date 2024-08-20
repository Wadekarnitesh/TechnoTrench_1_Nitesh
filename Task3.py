#PASSWORD GENERATOR 
#
#
import random
import string

print("<-Sales Forecasting Password Generator->")

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(chars, k=length-4)
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
#    
