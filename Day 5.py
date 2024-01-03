import re

def convert_to_list(input_string):

    # Using re.split() to separate characters by space or equals sign
    result = re.split(r'[ :]', input_string)

    # Removing empty strings from the result
    result = [item for item in result if item]
    return result

def find_interval(text_sequence, intervals):
    # Iterate over the intervals to find which suits us
    for interval in intervals:
        seperated_intervals = convert_to_list(interval)
        if int(text_sequence)>=int(seperated_intervals[1]) and int(text_sequence)<int(seperated_intervals[1])+int(seperated_intervals[2]):
            return seperated_intervals
        
def map_anything(seed,interval):  
    try:
        # Calculate the distance between seed and lowest interval
        difference = int(seed)-int(interval[1])
        
        # Add that distanfe to the soil's lowest interval
        return int(interval[0])+difference
    except TypeError:
        return seed

if __name__ == "__main__":

    text_sequence = list(open('day5-input.txt', 'r').read().split('\n'))

    converted_texts = convert_to_list(text_sequence[0])[1:]
    output_list = []
    for txt in converted_texts:
        interval_seed_to_soil = find_interval(txt,text_sequence[3:51])
        output = map_anything(txt,interval_seed_to_soil)

        interval_soil_to_fertilizer = find_interval(output,text_sequence[53:86])
        output = map_anything(output,interval_soil_to_fertilizer)

        interval_fertilizer_to_water = find_interval(output,text_sequence[88:98])
        output = map_anything(output,interval_fertilizer_to_water)

        interval_water_to_light = find_interval(output,text_sequence[100:112])
        output = map_anything(output,interval_water_to_light)

        interval_light_to_tempreture = find_interval(output,text_sequence[114:137])
        output = map_anything(output,interval_light_to_tempreture)

        interval_tempreture_to_humidity = find_interval(output,text_sequence[139:162])
        output = map_anything(output,interval_tempreture_to_humidity)

        interval_humidity_to_location = find_interval(output,text_sequence[179:213])
        output = map_anything(output,interval_humidity_to_location)

        output_list.append(output)

    print(min(output_list))