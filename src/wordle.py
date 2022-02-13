import argparse
import os
import string

DICT = 'dict.txt'
FIVE_LETTERS_WORDS = 'five-letter-words.txt'
SOURCE_ROOT = os.path.dirname(os.path.abspath(__file__))


def toFiveLetterWords():
    with open(DICT) as src:
        with open(FIVE_LETTERS_WORDS, 'w') as target:
            target.write(''.join([line for line in src if len(line) == 6]))


def contains(word, chars):
    return all([c in word for c in chars])


def notcontains(word, chars):
    return all([not c in word for c in chars])


def startswith(word, chars):
    return word.startswith(chars)


def pos2(word, chars):
    return word[1] == chars


def pos3(word, chars):
    return word[2] == chars


def pos4(word, chars):
    return word[3] == chars


def endswith(word, chars):
    return word.endswith(chars)


def weight(word, histo):
    return sum([histo[c] for c in word])


def getHistogram():
    histo = dict([(c, 0) for c in string.ascii_lowercase])
    with open(os.path.join(SOURCE_ROOT, FIVE_LETTERS_WORDS)) as f:
        for word in f.readlines():
            for i in range(5):
                histo[word[i]] += 1
    return histo


def toUniqueCharWords(list):
    return [word for word in list if len(set(word.strip())) == 5]


def sortByWeight(list, histo):
    return [word for (word, _) in sorted([(word, weight(word.strip(), histo))
                                          for word in list], key=lambda t: t[1], reverse=True)]


def positions(word, pos):
    return all([c == word[i] for(c, i) in pos])


def main_func():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--contains",
                        help="Search 5 letter words containing given letters")
    parser.add_argument("-n", "--notcontains",
                        help="Search 5 letter words not containing given letters")
    parser.add_argument(
        "-s", "--startswith", help="Search 5 letter words starting with given letters")
    parser.add_argument("-e", "--endswith",
                        help="Search 5 letter words ending with given letters")
    parser.add_argument("-2", "--pos2",
                        help="Search 5 letter words with given letter at second position")
    parser.add_argument("-3", "--pos3",
                        help="Search 5 letter words with given letter at third position")
    parser.add_argument("-4", "--pos4",
                        help="Search 5 letter words with given letter at forth position")
    parser.add_argument('-u', '--onlyUnique', action='store_true',
                        help='Only include words with unique letters')
    parser.add_argument('-w', '--sortByWeight', action='store_true',
                        help='Sort results by frequency of letters')
    parser.add_argument('-m', '--max', type=int,
                        help='Return only MAX results')
    parser.add_argument(
        '-p', '--pos', help='Search 5 letter words with letters on given position (e.g. ??ro)', default='')

    args = parser.parse_args()
    pos = [t for t in zip(args.pos, range(5)) if t[0]
           in string.ascii_lowercase]

    matchers = [matcher for matcher in [
        (startswith, args.startswith),
        (endswith, args.endswith),
        (contains, args.contains),
        (notcontains, args.notcontains),
        (pos2, args.pos2),
        (pos3, args.pos3),
        (pos4, args.pos4),
        (positions, pos)
    ] if matcher[1]]

    with open(os.path.join(SOURCE_ROOT, FIVE_LETTERS_WORDS)) as f:
        matches = [word for word in f.readlines() if all(
            [matcher(word.strip('\n'), _args) for (matcher, _args) in matchers])]

        if (args.onlyUnique):
            matches = toUniqueCharWords(matches)

        if (args.sortByWeight):
            matches = sortByWeight(matches, getHistogram())

        if (args.max):
            matches = matches[0:args.max]

        print(''.join(matches))


if __name__ == "__main__":
    # charHisto()
    main_func()
