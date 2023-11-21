def validate_numbers(numbers):
    print("Validating numbers...")
    valid_numbers = [num for num in numbers if isinstance(num, int)]
    print("Numbers validated.")
    return valid_numbers
