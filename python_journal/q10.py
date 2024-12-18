def mean(numbers):
    if len(numbers)==0:
        raise ValueError("The list shouldn't be empty.")
    
    return sum(numbers)/len(numbers)

def median(numbers):
    if len(numbers)==0:
        raise ValueError("The list cannot be empty.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n%2==1:
        return sorted_numbers[n//2]
    else:
        mid1 = sorted_numbers[n//2 - 1]
        mid2 = sorted_numbers[n//2]
        return sorted_numbers[(mid1+mid2)//2]

def mode(numbers):
    """Calculate the mode (most frequent element) of a list of numbers."""
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find the most frequent value(s)
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    return modes