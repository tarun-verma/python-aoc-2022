
def overlap(f) -> int:
    total_overlaps = 0
    for line in f:
        line = line.rstrip()
        elf1_sec, elf2_sec = line.split(',')
        elf1_low, elf1_up = elf1_sec.split('-')
        elf1_range = list(range(int(elf1_low), int(elf1_up)+1))
        elf2_low, elf2_up = elf2_sec.split('-')
        elf2_range = list(range(int(elf2_low), int(elf2_up)+1))
        if (len(set(elf1_range).intersection(set(elf2_range))) > 0) or (len(set(elf2_range).intersection(set(elf1_range))) > 0):
            total_overlaps += 1
    
    return total_overlaps

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(overlap(f))