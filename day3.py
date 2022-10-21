def split_to_bits(binary):
    return list(binary)


def get_gamma_epsilon(input_file_name):
    f = open(input_file_name, "r")
    diagnostic_report = list(f.read().splitlines())

    binary_bits = list(map(split_to_bits, diagnostic_report))
    binary_length = len(binary_bits[0])

    gamma = []
    epsilon = []
    for i in range(0, binary_length):
        zeros = 0
        ones = 0
        for binary in binary_bits:
            if binary[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    print("gamma:", gamma)
    print("epsilon:", epsilon)
    return gamma, epsilon, binary_length


def binary_to_decimal(bit_arr, binary_length):
    decimal = 0
    for bit in bit_arr:
        decimal += bit*pow(2, binary_length-1)
        binary_length -= 1
    return decimal


def get_power_consumption():
    gamma, epsilon, binary_length = get_gamma_epsilon("diagnosticReport.txt")
    gamma_decimal = binary_to_decimal(gamma, binary_length)
    epsilon_decimal = binary_to_decimal(epsilon, binary_length)
    power_consumption = gamma_decimal*epsilon_decimal
    print(power_consumption)
    return power_consumption


get_power_consumption()
