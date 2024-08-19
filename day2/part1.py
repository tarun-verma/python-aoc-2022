def totalscore(f) -> int:
    '''
    A B C = X Y Z = Rock, Paper, Scissors
    '''
    sel_dict = {'X':1, 'Y':2, 'Z':3}
    score = 0
    for line in f:
        line = line.rstrip()
        opp, me = line.split(' ')

        score += sel_dict[me]
        
        # draw
        if (opp == 'A' and me == 'X') or (opp == 'B' and me == 'Y') or (opp == 'C' and me == 'Z'):
            score += 3
        
        # win
        if (opp == 'A' and me == 'Y') or (opp == 'B' and me == 'Z') or (opp == 'C' and me == 'X'):
            score += 6

    return score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(totalscore(f))