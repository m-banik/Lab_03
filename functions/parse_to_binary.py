def parse_to_binary(input_number: int):
    if input_number == 0:
      return input_number
    binary_result = ''
    powers_of_two: list[int] = []
    checked_number = input_number
    while True:
        for i in range(1, checked_number):
            binary = 2
            for _ in range(1, i):
              binary *= 2
            if binary >= checked_number:
                if binary == input_number:
                  binary_result += "1"
                  binary = int(binary/2)
                  while True:
                    if binary == 0:
                      return int(binary_result)
                    binary_result += "0"
                    binary = int(binary/2)
                powers_of_two.append(int(binary/2))
                break
        if powers_of_two[len(powers_of_two) - 1] == 1:
          break
        checked_number = powers_of_two[len(powers_of_two) - 1]
    checked_number = 0
    for i in range(0, len(powers_of_two)):
        if checked_number + powers_of_two[i] <= input_number:
            checked_number += powers_of_two[i] 
            binary_result += "1"
            continue
        binary_result += "0"
    return int(binary_result)

