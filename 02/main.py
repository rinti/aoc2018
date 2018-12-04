from collections import Counter

with open('./input.txt', 'r') as f:
    lines = list(f.readlines())
    lines = list(map(lambda x: x.rstrip(), lines))
    lines = list(map(lambda x: Counter(list(x)), lines))

    def char_counter(char_count, line):
        return any(list(filter(lambda x: x == char_count, line.values())))

    def char_counter_twos(line):
        return char_counter(2, line)

    def char_counter_threes(line):
        return char_counter(3, line)

    threes = len(list(filter(char_counter_threes, lines.copy())))
    twos = len(list(filter(char_counter_twos, lines.copy())))

    # First problem:
    print(twos * threes)
