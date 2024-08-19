def max_calories(f) -> int:
    maxcals = 0
    sumsofar = 0

    for line in f:
        if line == '' or line == '\n':
            maxcals = max(sumsofar, maxcals)
            sumsofar = 0
        else:
            sumsofar += int(line.rstrip())
    
    return maxcals

if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        print(max_calories(f))