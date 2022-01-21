def find_by_boyer_and_moore(text: str, phrase: str, number_of_chars: int = 256):
    # Funkcja ma zwracać listę indeksów.
    found_indexes: list[int] = []
    phrase_length = len(phrase)
    text_length = len(text)
    incorrect_char = [-1]*number_of_chars
    for i in range(phrase_length):
      incorrect_char[ord(text[i])] = i
    index = 0
    while(index <= text_length-phrase_length):
        j = phrase_length - 1
        while j >= 0 and phrase[j] == text[index + j]:
            j -= 1
        if j < 0:
            found_indexes.append(index)
            index += (phrase_length-incorrect_char[ord(text[index+phrase_length])] if index+phrase_length<text_length else 1)
        else:
            index += max(1, j - incorrect_char[ord(text[index + j])])
    return found_indexes

