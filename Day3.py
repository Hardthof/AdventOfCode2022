class Decoder1:
    def __init__(self, seq, values):

        result = 0
        for s in seq: 
            matches = set()
            i = len(s) // 2
            for c in s[:i]:
                if c in s[i:]:
                    matches.add(c)
            result = result + sum([values[m] for m in matches])
        print(result)

class Decoder2:
    def __init__(self, seq, values):
        result = 0
        for i in range(0, len(seq), 3):
            result = result + values[list(set(seq[i]).intersection(set(seq[i+1]).intersection(set(seq[i+2]))))[0]]
        print(result)        


if __name__ == '__main__':

    f = open('Day3.txt', mode='r')
    seq = [line.strip() for line in f]

    values = {chr(ascii_value): ascii_value - ord('a') + 1 for ascii_value in range(ord('a'), ord('z') + 1)}
    values.update({chr(ascii_value): ascii_value - ord('A') + 27 for ascii_value in range(ord('A'), ord('Z') + 1)})
    
    Decoder1(seq, values)
    Decoder2(seq, values)
