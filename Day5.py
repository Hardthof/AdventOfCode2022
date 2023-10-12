import cProfile
import re
import math 

class Decoder1:
    def __init__(self, seq):
        print (sum([values[key] for key in seq]))

class Decoder2:
    def __init__(self, seq):
        print (sum([ruleSet2[key] for key in seq]))

def ApplyMove(cargo, move):
    numbers = re.findall(r'-?\d+\.\d+|\d+', move)
    numbers = [int(num) if num.isdigit() else float(num) for num in numbers]
    # print(m, numbers, cargo)

    for _ in range(numbers[0]):
        cargo[numbers[2]-1].append(cargo[numbers[1]-1].pop())

    # print(cargo)

def ApplyMove9001(cargo, move):
    numbers = re.findall(r'-?\d+\.\d+|\d+', move)
    numbers = [int(num) if num.isdigit() else float(num) for num in numbers]

    cut = numbers[0]
    cargo[numbers[2]-1].extend(cargo[numbers[1]-1][-cut:])
    cargo[numbers[1]-1] = cargo[numbers[1]-1][:-cut]

if __name__ == '__main__':

    f = open('Day5.txt', mode='r')
    seq = [line.replace('\n', '') for line in f]

    emptyLine = None

    for i,l in enumerate(seq):
        if l == '':
           emptyLine = i
           break

    # print(seq[i-1].split(' '))
    numBays = int(max([n.strip() for n in seq[i-1].split(' ')]))
             
    cargo = (seq[:i-1])
    moves = (seq[i+1:])

    cargoList = {}

    for i in range(numBays):
        cargoList[i] = []
        for j in range(len(cargo)):
            if cargo[-(1+j)][1+i*4] != ' ':
                cargoList[i].append(cargo[-(1+j)][1+i*4])
            else:
                break

    for m in moves:
        ApplyMove9001(cargoList, m)

    res = '' 
    for i in range(numBays):
        res = res + (cargoList[i].pop())
    print(res)
