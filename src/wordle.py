import argparse
import os

DICT = 'dict.txt'
FIVE_LETTERS_WORDS = 'five-letter-words.txt'
SOURCE_ROOT = os.path.dirname(os.path.abspath(__file__))


def toFiveLetterWords():
    with open(DICT) as src:
        with open(FIVE_LETTERS_WORDS, 'w') as target:
            target.write(''.join([line for line in src if len(line) == 6]))


def containsChars(word, chars):
    return all([c in word for c in chars])


def startswithChars(word, chars):
    return word.startswith(chars)


def endswithChars(word, chars):
    return word.endswith(chars)


def main_func():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--contains",
                        help="Search 5 letter words containing given letters")
    parser.add_argument(
        "-s", "--startswith", help="Search 5 letter words starting with given letters")
    parser.add_argument("-e", "--endswith",
                        help="Search 5 letter words ending with given letters")
    args = parser.parse_args()
    matchers = [matcher for matcher in [(startswithChars, args.startswith), (
        containsChars, args.contains), (endswithChars, args.endswith)] if matcher[1]]
    with open(os.path.join(SOURCE_ROOT, FIVE_LETTERS_WORDS)) as f:
        matches = [word for word in f.readlines() if all(
            [matcher(word.strip('\n'), chars) for (matcher, chars) in matchers])]
        print(''.join(matches))


if __name__ == "__main__":
    main_func()
