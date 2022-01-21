from .parse_to_binary import parse_to_binary
from .parse_to_decimal import parse_to_decimal


def encrypt_by_negative(input_text: str):
    as_ascii_code = ord(input_text)
    binary = parse_to_binary(as_ascii_code)
    as_byte_code = ""
    if len(str(binary)) < 8:
        for _ in range(len(str(binary)),  8):
            as_byte_code += "0"
    as_byte_code += str(binary)
    encrypted = ""
    for number in as_byte_code:
        if number == "1":
            encrypted += "0"
            continue
        encrypted += "1"
    as_decimal = parse_to_decimal(int(encrypted))
    # Do tego momentu algorytm działa w pełni poprawnie.
    # Natomiast Python jakby ignoruje wykonanie poniżej linii lub zwraca pusty string dla liczb dziesiętnych powyżej 127.
    # Nie wiem, dlaczego tak się dzieje i nie znalazłem solucji w sieci...
    encrypted = chr(as_decimal)
    return encrypted

