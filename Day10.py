if __name__ == '__main__':

    f = open('Day10.txt', mode='r')
    seq = [line.strip() for line in f]
    extendedSeq = []
    current_x = 1
    result = 0
    crt = ''

    for i, line in enumerate(seq):
        extendedSeq.append(current_x)
        if line.startswith('addx'):
            extendedSeq.append(current_x)
            current_x += int(line.split(' ')[1])

    for i in range(19, 220, 40):
        result += extendedSeq[i] * (i+1)
    print(result)

    for i in range(240):
        if abs(extendedSeq[i] - (i%40)) < 2:
            crt += '#'
        else:
            crt += '.'
        if (i+1) % 40 == 0: 
            print(crt)
            crt = ''