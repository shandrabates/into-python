"""
Simulate 6000 rolls of die (1-6)
"""

import random
import statistics

def roll_die(num):
    """
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 -> One, 1 -> 2, 2 -> 3, etc
    """
    freq = [0]*6   # list of initial value counts
    for roll in range(num):
        roll = random.randint(1,6)
        freq[roll-1] += 1
        #print(roll)
    return freq


def main():
    """
    test function
    :return: nothing
    """
    num = int(input("How many times do you want to roll"))
    l = roll_die(num)
    for roll,total in enumerate(l):
        print("Total rolls of {} = {}".format(roll+1, total))
    print("Average = {}".format(sum(l)/len(l)))
    print("Mean = {}".format(statistics.mean(l)))
    print("Median = {}".format(statistics.median(l)))



if __name__ == '__main__':
    main()
    exit(0)