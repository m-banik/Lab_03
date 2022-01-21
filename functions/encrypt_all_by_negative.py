from .encrypt_by_negative import encrypt_by_negative


def encrypt_all_by_negative(input_text: str):
    encrypted_text = ""
    for i in range(0, len(input_text)):
        encrypted_text += encrypt_by_negative(input_text[i])
    return encrypted_text

