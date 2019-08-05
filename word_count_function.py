"""
We will use this files to figure out how to define and later call up functions
Learn about functions/definitions
Use the keyword: def <name>():

"""

from urllib.request import urlopen


def fetch_words(file):
    """  A function that takes a text file and performs a word count
    :param file: a text file
    :return: number of words
    """
    count = 0
    data = []       #empty list
    with urlopen(file) as story:
        for line in story:
            words = line.decode('utf-8').split() #must decode into strings and then separate with spaces
            #print(lists)
            for word in words:
                data.append(word)
    return(data)

def print_words(story_words):
    """
    Print elements of the list
    :param story_words:
    :return: nothing
    """
    for word in story_words:
        print(word)


def main():
    """
    Test function
    :return: nothing
    """
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print_words(words)

if __name__ == "__main__":
    main()
    exit(0)
