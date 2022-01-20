from .check_if_is_palindrome import check_if_is_palindrome


def check_file_for_palindromes(input_data_path = './assets/data.txt', output_data_path = "./assets/palindromes.txt"):
    data = open(input_data_path, "r")
    data = list(map(str, data))
    if len(data) == 0:
        print("Brak danych.")
        return
    palindromes: list[str] = []
    for i in range(0, len(data)):
        data[i] = data[i].rstrip("\n")
        if check_if_is_palindrome(data[i]) is True:
            palindromes.append(data[i])
    if len(palindromes) == 0:
        print("Nie znaleziono palindromów.")
        return
    output_text = ""
    for palindrome in palindromes:
        output_text += " " + palindrome
    data = open(output_data_path, "w")
    data.write(output_text)
    data.close()
    print("Znalezione palindromy zostały zapisane do pliku pod adresem:", output_data_path)

