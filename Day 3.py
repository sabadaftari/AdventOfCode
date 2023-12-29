
import re
from collections import Counter
import string

def find_surrounding_chars_for_digits(text, target_number):

    def get_surrounding_chars(line, index, length_of_num):
        surrounding_chars = []
        if 0 <= index < len(line):
            surrounding_chars.append(line[index-1])
            surrounding_chars.append(line[index+length_of_num])

        return surrounding_chars
    
    def get_surrounding_chars_up(line,index, length_of_num):
        surrounding_chars = []
        if 0 <= index < len(line):
            for idx in range(length_of_num):
                surrounding_chars.append(line[index+idx])

        return surrounding_chars

    def get_surrounding_chars_down(line,index, length_of_num):
        surrounding_chars = []
        if 0 <= index < len(line):
            for idx in range(length_of_num):
                surrounding_chars.append(line[index+idx])

        return surrounding_chars

    result = {}

    for row, line in enumerate(text.splitlines()):
        for match in re.finditer(r'\b\d+\b', line):
            current_number = int(match.group())
            if current_number == target_number:
                position = match.start()
                num_str = str(current_number)
                length_of_num = len(num_str)

                surroundings = {
                    'upper': [],
                    'down': [],
                    'current_line': get_surrounding_chars(line, position, length_of_num),
                    'upper_left': [],
                    'upper_right': [],
                    'down_left': [],
                    'down_right': []
                }

                # Upper
                if row > 0:
                    surroundings['upper'].extend(get_surrounding_chars_up(text.splitlines()[row - 1], position, length_of_num))

                # Down
                if row < len(text.splitlines()) - 1:
                    surroundings['down'].extend(get_surrounding_chars_down(text.splitlines()[row + 1], position, length_of_num))

                # Diagonals
                if position > 0:
                    # Upper left
                    if row > 0:
                        surroundings['upper_left'].append(text.splitlines()[row - 1][position - 1])

                    # Down left
                    if row < len(text.splitlines()) - 1:
                        surroundings['down_left'].append(text.splitlines()[row + 1][position - 1])

                if position < len(line) - 1:
                    # Upper right
                    if row > 0:
                        surroundings['upper_right'].append(text.splitlines()[row - 1][position + length_of_num])

                    # Down right
                    if row < len(text.splitlines()) - 1:
                        surroundings['down_right'].append(text.splitlines()[row + 1][position + length_of_num])

                result.setdefault(current_number, []).append({
                    'position': (row, position),
                    'length_of_num': length_of_num,
                    'surroundings': surroundings
                })

    return result

def contains_non_numeric_values(dictionary):
    output_list =[]
    for value in dictionary.values():
        if value:
            for v in value:
                if v in string.punctuation and v!="." and v!='\\':
                    output_list.append(True)
                else:
                    output_list.append(False)
    
    return any(value for value in output_list)




if __name__ == "__main__":

    text = open('day3-input.txt', 'r').read()
    # Use regular expression to find all numbers in the text
    numbers = [int(match.group()) for match in re.finditer(r'\b\d+\b', text)]

    # Organize numbers by their digit lengths
    distict_numbers = []
    for num in numbers:
        length = len(str(num))
        distict_numbers.append(num)
    final_list = []
    for tr in distict_numbers:
        # if tr==182:
            my_dict = find_surrounding_chars_for_digits(text, tr)
            for target in my_dict[tr]:
                if contains_non_numeric_values(target["surroundings"]):
                    final_list.append(tr)
                    print("The dictionary contains non-numeric values.")
                else:
                    print("The dictionary contains only numbers and '.'.")
    
    print("sum: ", sum(list(set(final_list))))
    
