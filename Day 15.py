import re

def convert_to_list(input_string):

    # Using re.split() to separate characters by space or equals sign
    result = re.split(r'[,]', input_string)

    # Removing empty strings from the result
    result = [item for item in result if item]
    return result

def modify_ascii_values(input_string):
    ascii_values = [ord(char) for char in input_string]
    modified_values=(ascii_values[0] * 17) % 256 
    for id, ascii_val in enumerate(ascii_values):
        if id==0:
            continue
        else:
            modified_values = ((ascii_val+modified_values) * 17) % 256 
    return modified_values

if __name__ == "__main__":


    text_sequence = list(open('day15-input.txt', 'r').read().split('\n'))

    converted_texts = convert_to_list(text_sequence[0])

    output = [modify_ascii_values(str) for str in converted_texts]

    print(sum(output))