# def tilt_platform(platform, direction):
#     rows = len(platform)
#     cols = len(platform[0])

#     tilted_platform = [['.' for _ in range(cols)] for _ in range(rows)]

#     if direction == 'north':
#         for j in range(cols):
#             new_column = []
#             for i in range(rows):
#                 if platform[i][j] == 'O':
#                     new_column.append('.')
#                 else:
#                     new_column.append(platform[i][j])
#             new_column += ['O'] * platform.count('.')
#             for i in range(rows):
#                 tilted_platform[i][j] = new_column[i]
#     elif direction == 'south':
#         for j in range(cols):
#             new_column = ['O'] * platform.count('.') + platform.count('#') * ['.']
#             for i in range(rows):
#                 if platform[i][j] == 'O':
#                     new_column.pop(0)
#             for i in range(rows):
#                 tilted_platform[i][j] = new_column[i]
#     elif direction == 'east':
#         for i in range(rows):
#             new_row = ['O'] * platform[i].count('.') + platform[i].count('#') * ['.']
#             for j in range(cols):
#                 if platform[i][j] == 'O':
#                     new_row.pop(0)
#             tilted_platform[i] = new_row
#     elif direction == 'west':
#         for i in range(rows):
#             new_row = []
#             for j in range(cols):
#                 if platform[i][j] == 'O':
#                     new_row.append('.')
#                 else:
#                     new_row.append(platform[i][j])
#             new_row += ['O'] * platform[i].count('.')
#             tilted_platform[i] = new_row

#     return tilted_platform

# def calculate_total_load(platform):
#     total_load = 0

#     for i in range(len(platform)):
#         for j in range(len(platform[i])):
#             if platform[i][j] == 'O':
#                 total_load += len(platform) - i

#     return total_load

# # Example usage with the provided input


#     input_platform = list(open('day14-input.txt', 'r').read().split('\n'))
#     platform_example = [
#     "O....#....",
#     "O.OO#....#",
#     ".....##...",
#     "OO.#O....O",
#     ".O.....O#.",
#     "O.#..O.#.#",
#     "..O..#O..O",
#     ".......O..",
#     "#....###..",
#     "#OO..#...."
# ]
#     tilted_platform = tilt_platform(platform_example, 'north')
#     total_load = calculate_total_load(tilted_platform)

#     print("Tilted Platform:")
#     for row in tilted_platform:
#         print(''.join(row))

#     print("\nTotal Load on North Support Beams:", total_load)
def move_rocks_up(platform):
    rows, cols = len(platform), len(platform[0])

    for j in range(cols):
        for i in range(1, rows):
            if platform[i][j] == 'O' and platform[i-1][j] == '.':
                platform[i-1][j] = 'O'
                platform[i][j] = '.'

def move_rocks_left(platform):
    rows, cols = len(platform), len(platform[0])

    for i in range(rows):
        for j in range(1, cols):
            if platform[i][j] == 'O' and platform[i][j-1] == '.':
                platform[i][j-1] = 'O'
                platform[i][j] = '.'

def move_rocks_right(platform):
    rows, cols = len(platform), len(platform[0])

    for i in range(rows):
        for j in range(cols - 1, 0, -1):
            if platform[i][j] == 'O' and platform[i][j-1] == '.':
                platform[i][j] = '.'
                platform[i][j-1] = 'O'

def move_rocks_down(platform):
    rows, cols = len(platform), len(platform[0])

    for j in range(cols):
        for i in range(rows - 1, 0, -1):
            if platform[i][j] == 'O' and platform[i-1][j] == '.':
                platform[i][j] = '.'
                platform[i-1][j] = 'O'

def calculate_rock_count_in_rows(platform):
    rock_counts = []

    for i in range(len(platform)):
        rock_count = platform[i].count('O')
        rock_counts.append(rock_count)

    return rock_counts
if __name__ == "__main__":
    input_platform = list(open('day14-input.txt', 'r').read().split('\n'))
    # Convert platform to a list of lists for easier modification
    platform_example_list = [list(row) for row in input_platform]

    print("Original Platform:")
    for row in platform_example_list:
        print(''.join(row))

    for i in range(1000000000):
        # Move rocks up 1000 times
        for _ in range(1000):
            move_rocks_up(platform_example_list)

        # Move rocks up 1000 times
        for _ in range(1000):
            move_rocks_left(platform_example_list)
        
        # Move rocks up 1000 times
        for _ in range(1000):
            move_rocks_down(platform_example_list)

        # Move rocks up 1000 times
        for _ in range(1000):
            move_rocks_right(platform_example_list)

    print("\nPlatform after Moving Rocks Up 10 times:")
    for row in platform_example_list:
        print(''.join(row))

    # Calculate rock count in each row and multiply by the row index
    rock_counts_in_rows = calculate_rock_count_in_rows(platform_example_list)

    print("\nRock Count in Each Row multiplied by Row Index:")
    final_result =0
    for i, count in enumerate(rock_counts_in_rows):
        result = count * (len(rock_counts_in_rows)- i)  # Multiply by the row index (1-based)
        print(f"Row {i + 1}: {count} * {len(rock_counts_in_rows)- i} = {result}")
        final_result+=result
        print(final_result)






