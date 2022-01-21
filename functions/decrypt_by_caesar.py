from common.variables import key


def decrypt_by_caesar(text:str, used_key: int = key):
    decrypted = ""
    for i in range(0, len(text)):
        if ord(text[i]) - used_key > 122:
            decrypted += chr(ord(text[i]) - (used_key + 26))
        else:
            decrypted += chr(ord(text[i]) - used_key)
    return decrypted

