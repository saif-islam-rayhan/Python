
# 1. STRING BASICS & CREATION

single_quotes = 'Hello World'
double_quotes = "Python Programming"
triple_quotes = """This is a
multi-line string"""
raw_string = r'C:\new_folder'  # Escape characters ignored

print(single_quotes)
print(double_quotes)
print(triple_quotes)
print(raw_string)


# 2. STRING INDEXING & SLICING (SUBSTRINGS)

text = "PythonProgramming"

# Positive indexing (0-based)
print(text[0])     # 'P' (first character)
print(text[6])     # 'P' (7th character)

# Negative indexing (from end)
print(text[-1])    # 'g' (last character)
print(text[-3])    # 'i' (3rd from last)

# Slicing [start:end:step]
print(text[0:6])   # 'Python'
print(text[6:])    # 'Programming'
print(text[:6])    # 'Python'
print(text[::2])   # 'Pto rgamn' (every 2nd character)
print(text[::-1])  # 'gnimmargorPnohtyP' (reverse string)


# 3. STRING MODIFICATION METHODS

original = "  Hello, World!  "

# Case modification
print(original.lower())       # "  hello, world!  "
print(original.upper())       # "  HELLO, WORLD!  "
print(original.title())       # "  Hello, World!  "
print(original.capitalize())  # "  hello, world!  "
print(original.swapcase())    # "  hELLO, wORLD!  "

# Whitespace handling
print(original.strip())      # "Hello, World!"
print(original.lstrip())     # "Hello, World!  "
print(original.rstrip())     # "  Hello, World!"

# Replacement
print(original.replace("World", "Python"))  # "  Hello, Python!  "
print("a-b-c".replace("-", ""))             # "abc"


# 4. STRING FORMATTING (4 METHODS)

name = "Alice"
age = 25

# 1. f-strings (Python 3.6+)
print(f"{name} is {age} years old")

# 2. format() method
print("{} is {} years old".format(name, age))

# 3. %-formatting (older style)
print("%s is %d years old" % (name, age))

# 4. Template strings
from string import Template
t = Template("$name is $age years old")
print(t.substitute(name=name, age=age))


# 5. STRING SEARCH & VALIDATION

s = "Python Programming"

# Search methods
print(s.find("Pro"))        # 7 (returns index)
print(s.index("Pro"))       # 7 (similar but raises ValueError if not found)
print(s.rfind("o"))         # 9 (last occurrence)
print("Pro" in s)           # True (membership check)
print(s.startswith("Py"))   # True
print(s.endswith("ing"))    # True

# Validation methods
print("abc123".isalnum())   # True (letters or numbers)
print("abc".isalpha())      # True (letters only)
print("123".isdigit())      # True (digits only)
print("python".islower())   # True
print("PYTHON".isupper())   # True
print("Title Case".istitle()) # True

# 6. STRING SPLITTING & JOINING

data = "apple,orange,banana"

# Splitting
print(data.split(","))       # ['apple', 'orange', 'banana']
print(data.rsplit(",", 1))   # ['apple,orange', 'banana'] (from right)
print("1 2 3".split())       # ['1', '2', '3'] (default splits on whitespace)

# Joining
words = ["Python", "is", "awesome"]
print(" ".join(words))       # "Python is awesome"
print("-".join(words))       # "Python-is-awesome"


# 7. STRING PADDING & ALIGNMENT

text = "Python"

print(text.ljust(10, "*"))   # "Python****"
print(text.rjust(10, "*"))   # "****Python"
print(text.center(10, "*"))  # "**Python**"

# Zero padding for numbers
num = "42"
print(num.zfill(5))          # "00042"

# 8. CHARACTER ENCODING & BYTES

# String to bytes
byte_data = "Python".encode('utf-8')
print(byte_data)             # b'Python'

# Bytes to string
decoded = byte_data.decode('utf-8')
print(decoded)               # "Python"

# 9. ADVANCED STRING OPERATIONS

# Counting substrings
print("hello hello".count("hel"))  # 2

# Partitioning
print("python.is.awesome".partition("."))  # ('python', '.', 'is.awesome')

# Translation table
trans = str.maketrans("aeiou", "12345")
print("apple".translate(trans))    # "1ppl2"


# 10. REAL-WORLD EXAMPLES

# 1. Password validator
password = "Python3$"
if (len(password) >= 8 and 
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password)):
    print("Valid password")
else:
    print("Invalid password")

# 2. Palindrome checker
def is_palindrome(s):
    return s == s[::-1]
    
print(is_palindrome("madam"))  # True

# 3. Extract domain from email
email = "user@example.com"
domain = email.split("@")[-1]
print(domain)  # "example.com"