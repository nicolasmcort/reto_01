def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        # Check if the number is divisible by any number between 2 and itself
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    numbers = list(map (int, input("Enter a list of numbers separated by spaces: ").split())) 
    prime_numbers = []
    
    for num_str in numbers:
        # Check if the input is a valid number
        try:
            num = int(num_str) 
            if is_prime(num):
                prime_numbers.append(num)
        except ValueError: 
            print(f"'{num_str}' is not a valid number.") # Invalid input

    print(f"In your list, the prime numbers are: {prime_numbers}")
