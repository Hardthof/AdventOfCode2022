import cProfile

class Decoder1:
    def __init__(self, seq):
        print(max( [sum(map(int, s)) for s in seq] ))


if __name__ == '__main__':

    f = open('Day1.txt', mode='r')
    seq = [x.split('\n') for x in f.read().split('\n\n')]
    #cProfile.run('Decoder1(seq)')
    Decoder1(seq)
