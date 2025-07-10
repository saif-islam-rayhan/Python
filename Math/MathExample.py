import math
number = 25
print(math.sqrt(number))  # Output: 5.0

#Pow
x, y = 2, 3
print(math.pow(x, y))  # Output: 8.0

#Factorial
n = 5
print(math.factorial(n))  # Output: 120

#Celling
num = 3.14
print(math.ceil(num))  # Output: 4

#Floor
num = 3.99
print(math.floor(num))  # Output: 3

#Sine
angle = math.pi / 2  # 90 degrees in radians
print(math.sin(angle))  # Output: 1.0

#Cosine
angle = math.pi  # 180 degrees in radians
print(math.cos(angle))  # Output: -1.0

#Tan
angle = math.pi / 4  # 45 degrees in radians
print(math.tan(angle))  # Output: 0.9999999999999999 (~1.0)

#Degrees to Radians
degrees = 180
print(math.radians(degrees))  # Output: 3.141592653589793 (π)

#Radians to Degrees
radians = math.pi
print(math.degrees(radians)) 

#Absolute Value
num = -5.5
print(math.fabs(num))  # Output: 5.5

#Log  Base e
num = 10
print(math.log(num))  # Output: 2.302585092994046

#Logarithm – Base 10
num = 100
print(math.log10(num))  # Output: 2.0

#Combination – nCr  
n, r = 5, 2
print(math.comb(n, r))  # Output: 10

#Permutation – nPr
n, r = 5, 2
print(math.perm(n, r))  # Output: 20