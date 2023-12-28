def text_to_matrix(text):
    rows = len(text)
    cols = max(map(len, text.splitlines()))  # Assume the text is organized in lines

    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

    for i, line in enumerate(text.splitlines()):
        for j, char in enumerate(line):
            matrix[i][j] = char

    return matrix

# Example usage
text_example = open('day3-input.txt', 'r').read()

# matrix_example = text_to_matrix(text_example)

# # Print the matrix
# for row in matrix_example:
#     print(row)
import re
def find_surrounding_chars(text):
    numbers = [int(num) for num in re.findall(r'\b\d+\b', text)]

    def get_surrounding_chars(line, index):
        surrounding_chars = []
        if 0 <= index < len(line):
            surrounding_chars.append(line[index])
            if index > 0:
                surrounding_chars.append(line[index - 1])  # Left
            if index < len(line) - 1:
                surrounding_chars.append(line[index + 1])  # Right

        return surrounding_chars

    result = {}
    for num in numbers:
        positions = [m.start() for m in re.finditer(r'\b' + str(num) + r'\b', text)]
        result[num] = []

        for position in positions:
            lines = text.splitlines()
            row, col = 0, 0
            for i, line in enumerate(lines):
                if position < col + len(line):
                    row = i
                    break
                col += len(line) + 1

            # Upper
            if row > 0:
                result[num].extend(get_surrounding_chars(lines[row - 1], position - col))

            # Down
            if row < len(lines) - 1:
                result[num].extend(get_surrounding_chars(lines[row + 1], position - col))

            # Current line
            result[num].extend(get_surrounding_chars(lines[row], position - col))

            # Diagonals
            if position > col:
                # Upper left
                if row > 0:
                    result[num].append(lines[row - 1][position - col - 1])

                # Down left
                if row < len(lines) - 1:
                    result[num].append(lines[row + 1][position - col - 1])

            if position < col + len(lines[row]) - 1:
                # Upper right
                if row > 0:
                    result[num].append(lines[row - 1][position - col + 1])

                # Down right
                if row < len(lines) - 1:
                    result[num].append(lines[row + 1][position - col + 1])

    return result

# Example usage
text_example = open('day3-input.txt', 'r').read()

result = find_surrounding_chars(text_example)

def contains_only_numbers_and_asterisk(lst):
    valid_characters = set('0123456789.')
    return all(char in valid_characters for char in lst)
num_list=[]
# Print the result
for num, chars in result.items():
    if contains_only_numbers_and_asterisk(chars):
        print("The list contains only numbers and '.'.")
        print("NO SHITET!")
    else:
        print("The list contains other characters besides numbers and '.'.")
        num_list.append(num)

final_result = sum(num_list)
print(final_result)

