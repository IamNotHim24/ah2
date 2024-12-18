def armstrong(num):
    num_digits = len(str(num))

    sum_of_pow = sum(int(digit) ** num_digits for digit in str(num))
    return sum_of_pow == num

asn = [num for num in range(100,999) if armstrong(num)]

print(asn)