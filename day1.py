def sonar_sweep(input_file_name):
    f = open(input_file_name, "r")
    measurements = list(map(int, f.read().splitlines()))

    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            count += 1
    print(count)

# sonar_sweep("measurementReport.txt")


def get_three_measurements_sum(measurements, i):
    return measurements[i] + measurements[i+1] + measurements[i+2]


def sonar_sweep_expanded(input_file_name):
    f = open(input_file_name, "r")
    measurements = list(map(int, f.read().splitlines()))

    # measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    count = 0
    for i in range(1, len(measurements)-2):
        if get_three_measurements_sum(measurements, i) > get_three_measurements_sum(measurements, i-1):
            count += 1
        i += 1
    print(count)


sonar_sweep_expanded("measurementReport.txt")