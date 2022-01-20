from random import randint
from .encrypt import encrypt
from .decrypt import decrypt


def encrypt_and_decrypt_by_mirroring(input_data_path = './assets/encrypt_me.txt'):
    data = open(input_data_path, "r")
    data = list(map(str, data))
    if len(data) == 0:
        print("Brak danych.")
        return
    combined_text = ""
    for line in data:
        combined_text += line
    print("Dane z pliku po połączniu w jeden teskt:")
    print(combined_text)
    print()
    reversed_text = ""
    for i in range(len(combined_text) - 1, -1, -1):
        reversed_text += combined_text[i]
    print("Dane z pliku po połączniu w jeden teskt i odwróceniu:")
    print(reversed_text)
    print()
    key = randint(1, 25)
    encrypted_text = encrypt(reversed_text, key)
    print("Dane z pliku po połączniu w jeden teskt, odwróceniu i zakodowaniu szyfrem Cezara:")
    print(encrypted_text)
    print()
    decrypted_text = decrypt(encrypted_text, key)
    print("Dane po odszyfrowaniu:")
    print(decrypted_text)
    print()
    result_after_parsing = ""
    for i in range(0, len(decrypted_text)):
        result_after_parsing += combined_text[i]
    print("Dane po odszyfrowaniu i odwróceniu do postaci wyjściowej:")
    print(result_after_parsing)

