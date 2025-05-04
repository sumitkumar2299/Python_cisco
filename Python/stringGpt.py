# 1. Creating Strings

name = "Sumit"
greeting = 'Hello'
# 2. Multiline Strings
# Use triple quotes:


# message = '''This is
# a multilin
# string.'''

# 3. String Concatenation

full = "Hello, " + name
print(full)  # Output: Hello, Sumit
# 4. String Formatting

age = 21
intro = f"My name is {name} and I am {age} years old."
print(intro)
# 5. Common String Methods

text = "hello world"
print(text.upper())    # 'HELLO WORLD'
print(text.capitalize())  # 'Hello world'
print(text.replace("world", "Python"))  # 'hello Python'
print(len(text))  # 11
# 6. String Indexing and Slicing

s = "Python"
print(s[0])    # 'P'
print(s[-1])   # 'n'
print(s[0:3])  # 'Pyt'