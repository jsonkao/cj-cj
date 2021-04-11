import sys

num_tests = int(next(sys.stdin))
case_num = 1

def solve(x, y, string):
    string = [c for c in string]
    while '?' in string:
        for i in range(len(string)):
            c = string[i]
            if c == '?':
                if string[i+1] == '?' or i == len(string) - 1:
                    string[i] = string[i-1]
                else:
                    string[i] = string[i + 1]
    # calc cost
    cost = 0
    for i in range(len(string) - 1):
        if string[i] == 'C' and string[i + 1] == 'J':
            cost += x
        if string[i] == 'J' and string[i + 1] == 'C':
            cost += y
    return cost

for _ in range(num_tests):
    line = next(sys.stdin);
    [x, y, string] = line.split(' ');
    x = int(x)
    y = int(y)
    print(f"Case #{case_num}: {solve(x, y, string)}")
    case_num += 1
