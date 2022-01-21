def find_all_by_brute_force(text: str, phrase: str, ignore_letter_size: bool = False):
    found_indexes: list[int] = []
    if len(phrase) <= len(text):
        for i in range(0, len(text)):
            scope = i + len(phrase)
            if scope > len(text):
                break
            sub_str = ""
            for j in range(i, scope):
                if ((ignore_letter_size is True and text[j].lower() != phrase[len(sub_str)].lower()) or
                    (ignore_letter_size is False and text[j] != phrase[len(sub_str)])):
                    break
                sub_str += text[j]
            if ((ignore_letter_size is True and sub_str.lower() == phrase.lower()) or
                (ignore_letter_size is False and sub_str == phrase)):
                found_indexes.append(i)
    return found_indexes

