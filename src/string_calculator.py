def add(numbers):
    if not numbers:
        return 0

    if numbers.startswith("//"):
        delimiter_section, numbers = numbers.split("\n", 1)
        delimiter = delimiter_section[2:]
    else:
        delimiter = ","
    
    numbers = numbers.replace("\n", delimiter)
    
    number_list = [int(num) for num in numbers.split(delimiter)]
    
    negatives = [num for num in number_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return sum(number_list)