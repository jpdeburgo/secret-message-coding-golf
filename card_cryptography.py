suits = ["C", "D", "H", "S"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
DECK = [rank + suit for suit in suits for rank in ranks]
ALPHABET = [' ', *[chr(ord('A') + i) for i in range(26)]]
def get_permutation_index(strings, target_permutation):
    # Helper function to find the index of a permutation
    def find_permutation_index(arr):
        count = 0
        for i in range(len(arr) - 1):
            smaller_count = sum(arr[j] < arr[i] for j in range(i + 1, len(arr)))
            count += smaller_count * factorial(len(arr) - i - 1)
        return count
    # Helper function to calculate factorial
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    # Calculate the index of the target permutation
    index = find_permutation_index([strings.index(s) for s in target_permutation])
    return index
def get_permutation_from_index(strings, index):
    n = len(strings)
    factorial = [1]
    factorial.extend(factorial[-1] * i for i in range(1, n))
    result = []
    available = list(strings)

    for i in range(n):
        quotient = index // factorial[n - i - 1]
        result.append(available.pop(quotient))
        index %= factorial[n - i - 1]

    return result
def get_message_index(message):
    index = 0
    power = len(message) - 1
    for letter in message:
        index += (ord(letter) - 64 if letter != " " else 0) * (27**power)
        power -= 1
    return index
def encode(message):
    return get_permutation_from_index(DECK, get_message_index(message))
def decode(encoded_message):
    index = get_permutation_index(DECK, encoded_message)
    message = ""
    while index > 0:
        message += ALPHABET[int(index % 27)]
        index //= 27
    return message[::-1]