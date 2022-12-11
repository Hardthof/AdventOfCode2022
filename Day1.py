import cProfile

class Decoder1:
    def __init__(self, seq):
        l = [sum(map(int, s)) for s in seq]
        print(max( l ))
        print(sum(sorted(l)[-3:]))


if __name__ == '__main__':

    f = open('Day1.txt', mode='r')
    seq = [x.split('\n') for x in f.read().split('\n\n')]
    #cProfile.run('Decoder1(seq)')
    Decoder1(seq)
