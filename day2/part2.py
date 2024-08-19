def totalscore(f) -> int:
    '''
    A B C = X Y Z = Rock, Paper, Scissors
    '''
    sel_dict = {'X':1, 'Y':2, 'Z':3}
    score = 0
    for line in f:
        line = line.rstrip()
        opp, me = line.split(' ')

        # lose
        if me == 'X':
            if opp == 'A':
                score += sel_dict['Z']
            elif opp == 'B':
                score += sel_dict['X']
            else:
                score += sel_dict['Y']
        # draw
        elif me == 'Y':
            if opp == 'A':
                score += sel_dict['X'] + 3
            elif opp == 'B':
                score += sel_dict['Y'] + 3
            else: 
                score += sel_dict['Z'] + 3
        
        # win
        elif me == 'Z':
            if opp == 'A':
                score += sel_dict['Y'] + 6
            elif opp == 'B':
                score += sel_dict['Z'] + 6
            else: 
                score += sel_dict['X'] + 6

    return score

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(totalscore(f))