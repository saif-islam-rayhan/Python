s1 = set(map(int, input("Enter elements of s1 separated by commas: ").split(',')))
s2 = set(map(int, input("Enter elements of s2 separated by commas: ").split(',')))

print("s1:", s1)
print("s2:", s2)
print("union:", s1 | s2)
print("intersection:", s1 & s2)
print("difference (s1 - s2):", s1 - s2)
print("difference (s2 - s1):", s2 - s1)
