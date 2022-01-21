from functions.check_if_is_palindrome import check_if_is_palindrome


def check_for_palindromes(input_text:str):
    found_palindromes: list[str] = []
    for i in range(0, len(input_text)):
        checked_text = ""
        for j in range(i, len(input_text)):
            checked_text += input_text[j]
            signs_of_checked_text: list[str] = []
            for letter in checked_text:
                already_exists = False
                for sign in signs_of_checked_text:
                    if sign == letter:
                        already_exists = True
                if already_exists is False:
                    signs_of_checked_text.append(letter)
            if len(signs_of_checked_text) > 1 and check_if_is_palindrome(checked_text) is True:
                found_palindromes.append(checked_text)
    # Dysponując pustą tablicą wiemy, że nie mamy palindromów w badanym tekście.
    if len(found_palindromes) == 0:
        return "Brak"
    longest_palindromes: list[str] = []
    for palindrome in found_palindromes:
        for sample in found_palindromes:
            if palindrome != sample and len(palindrome) > len(sample):
                is_new_element = True
                for longest_palindrome in longest_palindromes:
                    if longest_palindrome == palindrome:
                        is_new_element = False
                        break
                if is_new_element is True:
                    longest_palindromes.append(palindrome)
    # Zwracamy listę dwuwymiarową. Zawiera dwa elementy.
    # Pierwszy to właściwa lista znalezionych palindromów, drugi to lista najdłuższych.
    # Zdecydowałem się użyć listy również jako drugiego elementu, bo najdłuższe palindromy mogą mieć tę samą długość.
    return [found_palindromes, longest_palindromes]

