def check_if_is_anagram(text1: str, text2:str):
    if len(text1) == len(text2):
        for letter in text1:
          number_of_letters_in_text1 = 0
          number_of_letters_in_text2 = 0
          for i in text1:
            if letter == i:
                number_of_letters_in_text1 += 1
          for j in text2:
            if letter == j:
                number_of_letters_in_text2 += 1
          if number_of_letters_in_text1 != number_of_letters_in_text2:
              return False
        return True
    return False

