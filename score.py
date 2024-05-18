SCORE_FILE = 'scores.txt'

def read_scores(filename = SCORE_FILE):

    try:
        infile = open(filename, 'r')
        data = infile.read()
        infile.close()
        return data
    except FileNotFoundError:
        return ''
    except OSError:
        print('Could not open')
        return

def write_scores(new_data, filename = SCORE_FILE, mode = 'a'):

    try:
        outfile = open(filename, mode)
        outfile.write(new_data)
        outfile.close()
    except OSError:
        print('Could not open')
        return ''

def update_score(name, score, filename= SCORE_FILE):

    new_record = name + ' ' + str(score)
    new_data = new_record + '\n'
    scores_data = read_scores(filename)

    if scores_data == None:
        return ''

    if scores_data:
        records = scores_data.splitlines()
        high_scorer = records[0].rsplits('',1)
        try:
            high_scorer = int(high_scorer[1])
            if score > high_scorer:
                scores_data = new_data  + scores_data
                if write_scores(scores_data, filename, 'w') == '':
                    return ''
                else:
                    return new_record
        except ValueError:
            print("unknown format for the score file.")
            return ''
        if scores_data[-1]!='\n':
            new_data = '\n ' + new_data

    if write_scores(new_data, filename) == '':
        return ''
    else:
        return new_record