import re

def extract_numbers(input_string):
    # Use a regular expression to find all numbers in the string
    numbers = re.findall(r'\d+', input_string)
    return [int(num) for num in numbers]

def calculate_points(card):

    # Split the string by "|" and ":"
    result = re.split(r'[|:]', card)

    first_part = extract_numbers(result[1])
    second_part = extract_numbers(result[2])

    exist_list = [True for f in first_part if f in second_part]

    # Count the number of True values in the list
    count_true = exist_list.count(True)
    if count_true==0:
        print("Shiiiyyeeeeet")
        return 0
    else:
        return 2**(count_true-1)

if __name__ == "__main__":
    data = open('day4-input.txt', 'r').read().split('\n')

    result = [calculate_points(card) for card in data]

    print(sum(result))
