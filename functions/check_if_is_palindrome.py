def check_if_is_palindrome(text: str):
    i = 0
    for j in range(len(text) - 1, 0, -1):
        if text[i] != text[j]:
            return False
        i += 1
    return True

