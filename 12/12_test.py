import change as ch

if __name__ == '__main__':
    n = int(input('길이(cm) 입력 : '))

    res = ch.cm_mm(n)
    print(f'{n}cm\t:\t{res}mm')

    res = ch.cm_inch(n)
    print(f'{n}cm\t:\t{res}inch')

    res = ch.cm_M(n)
    print(f'{n}cm\t:\t{res}m')

    res = ch.cm_ft(n)
    print(f'{n}cm\t:\t{res}ft')