import re

def check_line(string):
    
    # Your input string
    input_string = string

    # Define a regular expression to match two characters before the word "green"
    pattern_green = re.compile(r'(..)\sgreen')
    pattern_blue = re.compile(r'(..)\sblue')
    pattern_red = re.compile(r'(..)\sred')

    # Use the regular expression to find the match
    match_green = pattern_green.findall(input_string) #max 13
    match_blue = pattern_blue.findall(input_string) #max 14
    match_red = pattern_red.findall(input_string) #max 12

    # Extract the matched characters
    if match_green:
        two_chars_before_green = []
        for number in match_green:
            if int(number) > 13:
                two_chars_before_green.append(False)
            else:
                two_chars_before_green.append(True)

    if match_blue:
        two_chars_before_blue = []
        for number in match_blue:
            if int(number) > 14:
                two_chars_before_blue.append(False)
            else:
                two_chars_before_blue.append(True)

    if match_red:
        two_chars_before_red = []
        for number in match_red:
            if int(number) > 12:
                two_chars_before_red.append(False)
            else:
                two_chars_before_red.append(True)

    if all(two_chars_before_green) and all(two_chars_before_blue) and all(two_chars_before_red):
        return 1
    else:
        pass

def check_max_per_game(input_string):

    # Define a regular expression to match two characters before the word "green"
    pattern_green = re.compile(r'(..)\sgreen')
    pattern_blue = re.compile(r'(..)\sblue')
    pattern_red = re.compile(r'(..)\sred')

    # Use the regular expression to find the match
    match_green = max(pattern_green.findall(input_string)) #max 13
    match_blue = max(pattern_blue.findall(input_string)) #max 14
    match_red = max(pattern_red.findall(input_string)) #max 12

    power_num = int(match_blue) * int(match_green) * int(match_red)

    return power_num

if __name__ == "__main__":
    data = open('day2_input.txt', 'r').read().split('\n')
    output = [[idx,check_line(d)] for idx, d in enumerate(data)]
    # Sum the first elements of sublists where the second element is not None
    result_sum = sum(sublist[0]+1 for sublist in output if sublist[1] is not None)
    # Display the result
    print(result_sum)

    #second part
    output = [[idx,check_max_per_game(d)] for idx, d in enumerate(data)]

    summation = sum(sublist[1] for sublist in output if sublist[1] is not None)

    # Display the result
    print(summation)
