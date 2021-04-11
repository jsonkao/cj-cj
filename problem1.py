import sys


def pattern_matching_old(num_patterns):
    max_length = 0
    longest_pattern = None
    patterns = []
    for _ in range(num_patterns):
        pattern = next(sys.stdin).rstrip()
        patterns.append(pattern)
        length = len(pattern)
        if length > max_length:
            max_length = length
            longest_pattern = pattern

    if all(p[1:] + "!" in longest_pattern + "!" for p in patterns):
        return "A" + longest_pattern[1:]
    return "*"


def pattern_matching(num_patterns):
    max_lengths = [0, 0]
    longest_patterns = ["", ""]
    pattern_lists = [[], []]
    for _ in range(num_patterns):
        patterns = next(sys.stdin).rstrip().split("*")
        for i in [0, 1]:
            p = patterns[i]
            if len(p) > 0:
                pattern_lists[i].append(p)
            if len(p) > max_lengths[i]:
                longest_patterns[i] = p
                max_lengths[i] = len(p)

    if all(
        all(
            longest_patterns[i].startswith(p)
            if i == 0
            else longest_patterns[i].endswith(p)
            for p in pattern_lists[i]
        )
        for i in [0, 1]
    ):
        return "".join(longest_patterns)
    return "*"


num_tests = int(next(sys.stdin))
case_num = 1

for _ in range(num_tests):
    num_patterns = int(next(sys.stdin))
    print(f"Case #{case_num}: {pattern_matching(num_patterns)}")
    case_num += 1
