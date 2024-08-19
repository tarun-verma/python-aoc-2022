import string

def total_priors(f) -> int:
    lowercase_priorities = {letter: idx + 1 for idx, letter in enumerate(string.ascii_lowercase)}
    uppercase_priorities = {letter: idx + 27 for idx, letter in enumerate(string.ascii_uppercase)}
    total_priorities = 0
    buffer = []
    for line in f:
        line = line.rstrip()
        if len(buffer) == 2:
            buffer.append(line)
            common = set(buffer[0]) & set(buffer[1]) & set(buffer[2])
            common = common.pop()
            if common in lowercase_priorities:
                total_priorities += lowercase_priorities[common]
            else:
                total_priorities += uppercase_priorities[common]
            buffer.clear()
        else:
            buffer.append(line)
    return total_priorities

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(total_priors(f))