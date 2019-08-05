"""
We will use this files to figure out how to define and later call up functions
Learn about functions/definitions
Use the keyword: def <name>():

"""

from urllib.request import urlopen


def fetch_items(file):
    """  A function that takes a text file and performs a word count
    :param file: a text file
    :return: number of words
    """
    count = 0
    data = []       #empty list
    with urlopen(file) as story:
        for line in story:
            items = line.decode('utf-8').split() #must decode into strings and then separate with spaces
            #print(lists)
            for item in items:
                data.append(item)
    return(data)

def print_items(story_words):
    """
    Print elements of the list
    :param story_words:
    :return: nothing
    """
    for word in story_words:
        print(item)


def main():
    """
    Test function
    :return: nothing
    """
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_items(file)
    print_items(items)

if __name__ == "__main__":
    main()
    exit(0)
