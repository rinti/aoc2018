from collections import Counter
from itertools import combinations

with open('./input.txt', 'r') as f:
    lines = list(f.readlines())
    lines = list(map(lambda x: x.rstrip(), lines))
    counter_lines = list(map(lambda x: Counter(list(x)), lines))

    def char_counter(char_count, line):
        return any(list(filter(lambda x: x == char_count, line.values())))

    def char_counter_twos(line):
        return char_counter(2, line)

    def char_counter_threes(line):
        return char_counter(3, line)

    threes = len(list(filter(char_counter_threes, counter_lines.copy())))
    twos = len(list(filter(char_counter_twos, counter_lines.copy())))

    # First problem:
    #print(twos * threes)
    
    for x, y in combinations(lines.copy(), 2):
        diff = 0
        for i, char in enumerate(x):
            if char != y[i]:
                diff += 1

                if diff > 1:
                    continue

        if diff == 1:
            print("".join(
                a for a, b in zip(x, y) if a == b
            ))
