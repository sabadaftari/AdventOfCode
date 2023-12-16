import numpy


def check_number_of_ways(Time, Distance):

    count = 0
    for x in range(Time):
        if x * (Time-x) >= Distance:
            count+=1
    return count

if __name__ == "__main__":
    # first part
    input_list = [
                    [56, 499],
                    [97, 2210],
                    [77, 1097],
                    [93, 1440]
                ]
    
    ways = [check_number_of_ways(time, dist) for time, dist in input_list]
    result = numpy.prod(ways)

    print("My puzzle results are here: ", result)

    #second part

    input_list_2 = [56977793, 499221010971440]
    way = check_number_of_ways(input_list_2[0], input_list_2[1])

    print("My second puzzle results are here: ", way)
