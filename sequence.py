def remove_duplicates(sequence):    
    seen = set()  # Initialize an empty set to keep track of seen items
    result = []    # Initialize an empty list to store unique items

    for item in sequence:  # Iterate through each item in the input sequence
        if item not in seen:  # Check if the item is not already seen
            seen.add(item)     # Add the item to the set of seen items
            result.append(item)  # Append the item to the result list

    return result  # Return the list containing unique items

#  print output results
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5])) 
print(remove_duplicates([5, 4, 3, 2, 1]))  
print(remove_duplicates(['a', 'b', 'a', 'c', 'b', 'd'])) 