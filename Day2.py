import cProfile

# A Rock, B Paper, C Scissors
# X Rock, Y Paper, Z Scissors
# 1 2 3
values = {'A X': 1 + 3, 
'A Y': 2 + 6, 
'A Z': 3 + 0,
'B X': 1 + 0,
'B Y': 2 + 3,
'B Z': 3 + 6,
'C X': 1 + 6,
'C Y': 2 + 0,
'C Z': 3 + 3}

# X lose, Y draw, Z win
ruleSet2 = {'A X': 0 + 3, 
'A Y': 3 + 1, 
'A Z': 6 + 2,
'B X': 0 + 1,
'B Y': 3 + 2,
'B Z': 6 + 3,
'C X': 0 + 2,
'C Y': 3 + 3,
'C Z': 6 + 1}


class Decoder1:
    def __init__(self, seq):
        print (sum([values[key] for key in seq]))

class Decoder2:
    def __init__(self, seq):
        print (sum([ruleSet2[key] for key in seq]))


if __name__ == '__main__':

    f = open('Day2.txt', mode='r')
    seq = [line.strip() for line in f]
    

    # seq = ['A Y', 'B X', 'C Z']
    Decoder1(seq)
    Decoder2(seq)
