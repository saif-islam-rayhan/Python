def find_duplicates(input_list):
    duplicates = []  
    seen = []        

    for item in input_list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.append(item)

    return duplicates

numbers = [1, 5, 6, 5, 1, 2, 3]
result = find_duplicates(numbers)
print("Duplicate elements:", result)
