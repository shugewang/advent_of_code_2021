def calculate_position(input_file_name):
    f = open(input_file_name, "r")
    planned_course = list(f.read().splitlines())

    horizontal = 0
    depth = 0
    aim = 0

    for command in planned_course:
        command_arr = command.split(" ")
        if command_arr[0] == "forward":
            horizontal += int(command_arr[1])
            depth += int(command_arr[1]) * aim
        if command_arr[0] == "up":
            aim -= int(command_arr[1])
        if command_arr[0] == "down":
            aim += int(command_arr[1])

    print(horizontal*depth)


calculate_position("plannedCourse.txt")
