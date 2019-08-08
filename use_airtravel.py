"""
Use the flight class
"""


from airtravel import Flight, Aircraft


def main():
    """
    test function
    :return: nothing
    """
    f1 = Flight("DL066")
    print(f1.number())
    f2 = Flight("AM013")
    print(f2.number())
    f3 = Flight("AP019")

    print(f3.number())
    print(f1.airline())
    print(f2.airline())
    print(f3.airline())
    # Could use notation: Flight.number(f1)

    a1 = Aircraft("G-EUP", "Boeing 737-800 Max", num_rows=32, num_seats_row=6)
    print(a1.registration(), a1.model())



if __name__ == '__main__':
    main()
    exit(0)