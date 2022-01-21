def parse_to_decimal(input_number:int):
    input_number_as_string = str(input_number)
    parsed_number = 0
    for i in range(0, len(input_number_as_string)):
        if input_number_as_string[len(input_number_as_string) -1 - i] == '1':
            if i == 0:
              helper = 1
            else:
              helper = 2
              for _ in range(0, i - 1):
                  helper *= 2
            parsed_number += helper
    return parsed_number

