import string

def total_priors(f) -> int:
    lowercase_priorities = {letter: idx + 1 for idx, letter in enumerate(string.ascii_lowercase)}
    uppercase_priorities = {letter: idx + 27 for idx, letter in enumerate(string.ascii_uppercase)}
    total_priorities = 0
    for line in f:
        line = line.rstrip()
        mid = len(line) // 2
        first = line[:mid]
        second = line[mid:]

        intersection = set(first) & set(second)
        intersection = intersection.pop()

        if intersection in lowercase_priorities:
            total_priorities += lowercase_priorities[intersection]
        else:
            total_priorities += uppercase_priorities[intersection]
        
    return total_priorities


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(total_priors(f))