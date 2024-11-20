# reto_01

**1. Operaciones básicas entre 2 números**
Se utilizó la estructura match (disponible desde Python 3.10) para gestionar las diferentes operaciones aritméticas. La función `operations` toma dos números y un operador como entrada, y dependiendo del operador (+, -, *, /), realiza la operación correspondiente. También se incluyó una verificación para evitar la división por cero.
```python
def operations(a, b, operator: str):
    match operator:  # Match case to check the operator
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "Cannot divide by zero"  # Check for division by zero
            return a / b
        case _:
            return "Invalid operator"


if __name__ == "__main__":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = operations(a, b, operator)
    print(f"The result is: {result}")
```

**2. Verificar si una palabra es un palíndromk**
Para verificar si una palabra es un palíndromo, primero se limpia la entrada al eliminar los espacios y convertir todos los caracteres a minúsculas. Luego, se hace uso de un bucle para comparar cada carácter desde el principio con su correspondiente desde el final de la palabra. Si cualquier par no coincide, la función devuelve False.
```python
def palindrome(word: str) -> bool:
    # Remove spaces and convert to lowercase for 
    word = word.replace(" ", "").lower()

    # Iterate through half of the word for comparison
    for i in range(len(word) // 2):
        # Compare the character at index i with its corresponding character from the end
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    word = input("Enter a word: ")
    if not word:  # Check if the input is empty
        print("Please enter a valid word.")
    else:
        print(f"Is the expression '{word}' a palindrome? {palindrome(word)}")
```

**3. Números primos en una lista**
La función `is_prime` verifica si un número es primo, iterando desde 2 hasta el número menos 1 para ver si tiene divisores. Luego, se procesa una lista de entradas, verificando si cada número es primo y manejando entradas inválidas con un bloque `try-except` para asegurar que solo se consideraran números válidos.
```python
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
```

**4. Mayor suma entre dos elementos consecutivos**
Para cada par de números consecutivos se calcula su suma y se mantiene un registro de la mayor suma encontrada. También se implementó una validación para asegurar que los datos de entrada sean números válidos antes de proceder con el cálculo.
```python
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
```

**5. Filtrar palabras con los mismos caracteres**
Para encontrar las palabras con los mismos caracteres, se utiliza la función `sorted()` para ordenar las letras de cada palabra y compararlas con las demás. Si dos palabras tienen las mismas letras, se agregan a la lista de resultados. 
```python
def has_same_characters(words: list) -> list:
    result = []
    for first_word in words:
        for second_word in words:
            if first_word != second_word and sorted(first_word) == sorted(second_word): # Check if the sorted characters are the same
                result.append(first_word)
                break
    return result

if __name__ == "__main__":
    user_input = input("Enter a list of words separated by commas: ")
    words = [word.strip() for word in user_input.split(",")]
    
    result = has_same_characters(words)
    print("Words with the same characters:", result)
```
