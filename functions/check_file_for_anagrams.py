from .check_if_is_anagram import check_if_is_anagram


def check_file_for_anagrams(input_data_path = './assets/data.txt', output_data_path = "./assets/anagrams.txt"):
    data = open(input_data_path, "r")
    data = list(map(str, data))
    if len(data) == 0:
        print("Brak danych.")
        return
    output_text = ""
    for i in range(0, len(data)):
        data[i] = data[i].rstrip("\n")
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if i == j:
              continue
            if check_if_is_anagram(data[i], data[j]) is True:
                output_text += data[i] + "[indeks " + str(i) + "], " + data[j] + "[indeks " + str(j) + "]\n"
    if len(output_text) == 0:
        print("Nie znaleziono anagramów.")
        return
    data = open(output_data_path, "w")
    data.write(output_text)
    data.close()
    print("Znalezione anagramy zostały zapisane do pliku pod adresem:", output_data_path)

