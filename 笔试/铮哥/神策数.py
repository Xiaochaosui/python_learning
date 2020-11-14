def shen(temple):
    i = 1
    count = 0
    num = []
    while count < temple:
        result = i
        while result % 3 == 0:
            result = result / 3
        while result % 5 == 0:
            result = result / 5
        while result % 11 == 0:
                result = result / 11
        if result == 1:
            count += 1
            num.append(i)
        i += 1
    print(num[-1])


if __name__ == '__main__':
    x = int(input())
    shen(x)
