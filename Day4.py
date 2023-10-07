import cProfile


class Decoder1:
    def __init__(self, seq):
        print (sum([values[key] for key in seq]))

class Decoder2:
    def __init__(self, seq):
        print (sum([ruleSet2[key] for key in seq]))


if __name__ == '__main__':

    f = open('Day4.txt', mode='r')
    seq = [line.strip() for line in f]

    count = 0
    count2 = 0
    for line in seq:
        l,r = (line.split(','))
        a,b = l.split('-')
        c,d = r.split('-')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if a <= d and b >= c:
            count2 = count2 + 1
            if (a <= c and b >= d) or (a >= c and b <= d):
                count = count + 1
                print(line)
    print(count, count2)

    #Decoder1(seq)
    # Decoder2(seq)
