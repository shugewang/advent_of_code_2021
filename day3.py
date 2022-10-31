def split_to_bits(binary):
    return list(binary)


def get_binary_bits_array(input_file_name):
    f = open(input_file_name, "r")
    diagnostic_report = list(f.read().splitlines())
    binary_bits_array = list(map(split_to_bits, diagnostic_report))
    binary_length = len(binary_bits_array[0])
    return binary_bits_array, binary_length


def get_most_common_value(binary_bits, position):
    zeros = 0
    ones = 0
    for binary in binary_bits:
        if binary[position] == "0":
            zeros += 1
        else:
            ones += 1
    most_common = 1 if ones > zeros else 0
    least_common = 1 if zeros > ones else 0
    return zeros, ones, most_common, least_common


def get_gamma_epsilon(binary_bits_array, binary_length):
    gamma = []
    epsilon = []
    for i in range(0, binary_length):
        zeros, ones, most_common, least_common = get_most_common_value(binary_bits_array, i)
        if most_common == 0:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    return gamma, epsilon


def binary_to_decimal(bit_arr, binary_length):
    decimal = 0
    for bit in bit_arr:
        decimal += bit*pow(2, binary_length-1)
        binary_length -= 1
    return decimal


def get_power_consumption():
    binary_bits_array, binary_length = get_binary_bits_array("diagnosticReportTest.txt")
    gamma, epsilon = get_gamma_epsilon(binary_bits_array, binary_length)
    gamma_decimal = binary_to_decimal(gamma, binary_length)
    epsilon_decimal = binary_to_decimal(epsilon, binary_length)
    power_consumption = gamma_decimal*epsilon_decimal
    print("power_consumption: ", power_consumption)


def filter_most_common(most_common, i):
    return lambda binary_bits: binary_bits[i] == str(most_common)


def get_oxygen_generator_rating(binary_bits_array, binary_length):
    for i in range(0, binary_length):
        zeros, ones, most_common, least_common = get_most_common_value(binary_bits_array, i)
        if zeros == ones:
            most_common = 1
        binary_bits_array = list(filter(filter_most_common(most_common, i), binary_bits_array))
    oxygen_generator_rating = list(map(int, binary_bits_array[0]))
    oxygen_generator_rating_decimal = binary_to_decimal(oxygen_generator_rating, binary_length)
    return oxygen_generator_rating_decimal


def get_CO2_scrubber_rating(binary_bits_array, binary_length):
    for i in range(0, binary_length):
        if len(binary_bits_array) > 1:
            zeros, ones, most_common, least_common = get_most_common_value(binary_bits_array, i)
            if zeros == ones:
                least_common = 0
            binary_bits_array = list(filter(filter_most_common(least_common, i), binary_bits_array))

    co2_scrubber_rating = list(map(int, binary_bits_array[0]))
    co2_scrubber_rating_decimal = binary_to_decimal(co2_scrubber_rating, binary_length)
    return co2_scrubber_rating_decimal


def get_life_support_rating():
    binary_bits_array, binary_length = get_binary_bits_array("diagnosticReport.txt")
    oxygen_generator_rating_decimal = get_oxygen_generator_rating(binary_bits_array, binary_length)
    co2_scrubber_rating_decimal = get_CO2_scrubber_rating(binary_bits_array, binary_length)
    life_support_rating = oxygen_generator_rating_decimal * co2_scrubber_rating_decimal
    print("life_support_rating:", life_support_rating)


get_power_consumption()
get_life_support_rating()
