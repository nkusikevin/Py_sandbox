import random
import string

def generate_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

length = int(input("Enter the length of the code: "))
code = generate_code(length)
print("Generated code:", code)
