def max_consecutive_sum(nums: list) -> int:  
    max_sum: float = 0  
    
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

if __name__ == "__main__":
    user_input = input("Enter a list of integers, separated by spaces: ")
    
    # Split the input into a list of strings and try to convert them to integers
    user_input_list = user_input.split()
    numbers = []
    
    # Check if all elements are valid integers
    for num_str in user_input_list:
        try:
            num = int(num_str)  
            numbers.append(num)  
        except ValueError:  # If conversion fails, notify the user and skip the element
            print(f"'{num_str}' is not a valid number.")
    
    # Only proceed if we have at least two valid numbers
    if len(numbers) >= 2:
        result = max_consecutive_sum(numbers)
        print(f"The maximum sum of two consecutive elements is: {result}")
    else:
        print("Please enter at least two valid integers.")
