def is_tidy(number):
    previous = int(number % 10)

    while number > 0:
        number = int(number / 10)
        n = int(number % 10)

        if n > previous:
            return False

        previous = n

    return True


def last_tidy(n):
    i = n

    while i >= 0:
        if is_tidy(i):
            return i

        i -= 1

    return i


if __name__ == '__main__':
    f = open('b_small.in')
    lines = [int(n.rstrip('\n')) for n in f.readlines()]
    f.close()

    cases = lines[1:]

    for i, case in enumerate(cases):
        last_tidy_num = str(last_tidy(case))

        print('case #{0}: {1}'.format(str(i + 1), last_tidy_num))
