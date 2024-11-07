SCRAMBLED_PATH = 'C:\\Users\\Eric\\OneDrive\\Documents\\Algorithms\\hw\\pattern_matching\\ScrambleText.txt'
STRAIGHT_PATH = 'C:\\Users\\Eric\\OneDrive\\Documents\\Algorithms\\hw\\pattern_matching\\StraightText.txt'


def lev(a: str, b: str):
    return len(a) if len(b) == 0 else (len(b) if len(a) == 0 else (lev(tail(a), tail(b)) if head(a) == head(b) else (1 + min(lev(tail(a), b), lev(a, tail(b)), lev(tail(a), tail(b))))))


# readable
def levenshtein(a: str, b: str):
    if len(b) == 0:
        return len(a)
    elif len(a) == 0:
        return len(b)
    elif head(a) == head(b):
        return levenshtein(tail(a), tail(b))
    else:
        return 1 + min(levenshtein(tail(a), b), levenshtein(a, tail(b)), levenshtein(tail(a), tail(b)))


def tail(s: str):
    return s[1:]


def head(s: str):
    return s[0]


def getWords(file):
    words = []

    for line in file:
        for word in line.split():
            if word.endswith('.'):
                word = word[:len(word) - 1]

            words.append(word.lower())

    return words        


if __name__ == "__main__":
    with open(SCRAMBLED_PATH, 'r') as scrambled_file, open(STRAIGHT_PATH, 'r') as straight_file:
        scrambled_words = getWords(scrambled_file)
        straight_words = getWords(straight_file)

        for i in range(len(scrambled_words)):
            print(f'Levenshtein({scrambled_words[i]}, {straight_words[i]}) = {lev(scrambled_words[i], straight_words[i])}')