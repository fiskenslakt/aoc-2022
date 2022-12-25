from aocd import lines

SNAFU_DECIMAL = {'-': -1, '=': -2}


def snafu_to_decimal(snafu):
    decimal = 0

    for i, digit in enumerate(reversed(snafu)):
        decimal_digit = int(digit) if digit.isdecimal() else SNAFU_DECIMAL[digit]
        decimal += 5**i * decimal_digit

    return decimal


def decimal_to_snafu(decimal):
    snafu = ''

    while decimal:
        decimal, r = divmod(decimal+2, 5)
        snafu += '=-012'[r]

    return snafu[::-1]


fuel_requirements = []
for snafu in lines:
    decimal = snafu_to_decimal(snafu)
    fuel_requirements.append(decimal)

decimal_sum = sum(fuel_requirements)
snafu_sum = decimal_to_snafu(decimal_sum)

print('Part 1:', snafu_sum)
print('Part 2: Merry Christmas!')
