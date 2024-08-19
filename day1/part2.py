def max_calories(f) -> int:
    sumsofar = 0
    calsum = []

    for line in f:
        if line == '' or line == '\n':
            calsum.append(sumsofar)
            sumsofar = 0
        else:
            sumsofar += int(line.rstrip())
    
    calsum = sorted(calsum)
    return calsum[-1] + calsum[-2] + calsum[-3]

if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        print(max_calories(f))