from functions.find_by_brute_force import find_by_brute_force
from functions.check_if_is_palindrome import check_if_is_palindrome
from functions.check_file_for_palindromes import check_file_for_palindromes
from functions.check_if_is_anagram import check_if_is_anagram
from functions.check_file_for_anagrams import check_file_for_anagrams
from functions.encrypt_by_caesar import encrypt_by_caesar
from functions.decrypt_by_caesar import decrypt_by_caesar
from functions.encrypt_and_decrypt_by_mirroring import encrypt_and_decrypt_by_mirroring


# Zadanie 1
print()
print("Zadanie 1")
print()

while True:
    try:
        text = input("Proszę podać badany ciąg znaków: ")
        phrase = input("Proszę podać szukany ciąg znaków: ")
        if len(phrase) > len(text):
          raise ValueError
        break
    except ValueError:
        print("Podano niepoprawne dane!")


sub_str_index = find_by_brute_force(text, phrase)
if sub_str_index < 0:
    print("Nie znaleziono wzorca.")
else:
    print("Indeks szukanego wzorca:", str(sub_str_index))


# Zadanie 2
print()
print("Zadanie 2")
print()

while True:
    try:
        phrase = input("Proszę podać badany ciąg znaków: ")
        break
    except ValueError:
        print("Podano niepoprawne dane!")


if check_if_is_palindrome(phrase) is True:
    print("Fraza jest palindromem.")
else:
    print("Fraza nie jest palindromem.")

check_file_for_palindromes()


# Zadanie 3
print()
print("Zadanie 3")
print()

while True:
    try:
        text1 = input("Proszę podać pierwszy wyraz: ")
        text2 = input("Proszę podać drugi wyraz: ")
        break
    except ValueError:
        print("Podano niepoprawne dane!")


if check_if_is_anagram(text1, text2) is True:
    print("Podane wyrazy są anagramami.")
else:
    print("Podane wyrazy nie są anagramami.")

check_file_for_anagrams()


# Zadanie 4
print()
print("Zadanie 4")
print()

while True:
    try:
        text = input("Proszę podać zadany ciąg znaków: ")
        key = int(input("Proszę podać liczbę z przedziału 1-25: "))
        if key < 1 or key > 25:
          raise ValueError
        break
    except ValueError:
        print("Podano niepoprawne dane!")


encrypted = encrypt_by_caesar(text, key)
print("Tekst zadany w postaci szyfrowanej:", encrypted)
print("Szyfr zdekodowany do postaci tekstu zadanego: ", decrypt_by_caesar(encrypted, key))


# Zadanie 5
print()
print("Zadanie 5")
print()

encrypt_and_decrypt_by_mirroring()

