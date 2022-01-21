from functions.find_all_by_brute_force import find_all_by_brute_force
from functions.check_for_palindromes import check_for_palindromes
from functions.find_by_boyer_and_moore import find_by_boyer_and_moore
from functions.parse_to_binary import parse_to_binary
from functions.parse_to_decimal import parse_to_decimal
from functions.encrypt_all_by_negative import encrypt_all_by_negative


# Zadanie 1.
print()
print("Zadanie 1")
print()

text = 'BAABABAAABAAB'
phrase = "AAB"
print(find_all_by_brute_force(text, phrase))


# Zadanie 2.
print()
print("Zadanie 2")
print()

text = 'CABCBABBB'
print(check_for_palindromes(text))
text = 'CABCABBB'
print(check_for_palindromes(text))


# Zadanie 3.
print()
print("Zadanie 3")
print()

text = 'CABCBABBBBAB'
phrase = "BAB"
print(find_by_boyer_and_moore(text, phrase))


# Zadanie 4.
print()
print("Zadanie 4")
print()

test_decimal_numbers = [569, 101, 96, 12, 10, 9, 8, 7, 6, 5, 4, 0]
test_binary_numbers = [1000111001, 1100101, 1100000, 1100, 1010, 1001, 1000, 111, 110, 101, 100, 0]

try:
    if len(test_decimal_numbers) != len(test_binary_numbers):
        raise AssertionError
    for i in range(0, len(test_decimal_numbers)):
        binary = parse_to_binary(test_decimal_numbers[i])
        assert binary == test_binary_numbers[i]
        decimal = parse_to_decimal(binary)
        assert decimal == test_decimal_numbers[i]
    print("Testy przeszły pomyślnie.")
except AssertionError:
    print("Testy nie przeszły pomyślnie!")


# Zadanie 5.
print()
print("Zadanie 5")
print()

test_text = "AAA"
print("Zdanie", test_text, "po zakodowaniu przez negatyw ma postać:")
print(encrypt_all_by_negative(test_text))

