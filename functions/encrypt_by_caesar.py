from common.variables import key


def encrypt_by_caesar(text:str, used_key: int = key):
    encrypted = ""
    for i in range(0, len(text)):
        if ord(text[i]) - used_key > 122:
            encrypted += chr(ord(text[i]) + used_key - 26)
        else:
            encrypted += chr(ord(text[i]) + used_key)
    return encrypted

