'''
We will use this files to figure out how to define and later call up functions
Learn about functions/definitions
Use the keyword: def <name>():

'''

from urllib.request import urlopen


def word_count():
    """  A function that takes a text file and performs a word count
    :param file: a text file
    :return: number of words
    """
    n = 0
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    with urlopen(file) as story:
        for line in story:
            words = line.decode('utf-8').split() #must decode into strings and then separate with spaces
            #print(lists)
            for word in words:
             n += 1

    print("total number of words", n)



def word_organize():
    """
    A function that takes in a text file and organizes/lists the resulting words with counts as a dictionary
    :param file: a text file
    :return: a dictionary of words organized
    """

    count = 0
    data ={}
    with urlopen(file) as story:
        for line in story:
            lists = line.decode('utf-8').split() #must decode into strings and then separate with spaces
            # print lists
            #print(lists)
            for list in lists:
                #check to see if key is already in the dictionary (data)
                if list in data:
                    data[list] +=1
                #if not, assign a new key
                else:
                    data[list] =1
                count += 1
    print("Total data", data)
    # Sort by key values
    for key in sorted(data.keys()):
        print(key, data[key])


def main():
    """
    Test function
    :return: nothing
    """
    word_count()

if __name__ == "__main__":
    main()
    exit(0)
