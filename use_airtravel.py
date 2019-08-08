"""
Use the flight class
"""


from airtravel import Flight, Aircraft

from pprint import pprint as pp


def main():
    """
    test function
    :return: nothing
    """
    f1 = Flight("SN066", Aircraft("G-EUP", "CRJ", num_rows=20, num_seats_row=4))
    pp(f1._seating)

    f1.allocate_seat("2A", "Jane Doe")
    pp(f1._seating)

    f1.allocate_seat("4D", "John Smith")
    pp(f1._seating)

    # f1.allocate_seat("22A", "Leila Smith")  check to see that the different types of errors work
    # pp(f1._seating)

    # f1 = Flight("DL066")
    # print(f1.number())
    # f2 = Flight("AM013")
    # print(f2.number())
    # f3 = Flight("AP019")

    # print(f3.number())
    # print(f1.airline())
    # print(f2.airline())
    # print(f3.airline())
    # # Could use notation: Flight.number(f1)

    # a1 = Aircraft("G-EUP", "Boeing 737-800 Max", num_rows=32, num_seats_row=6)
    # print(a1.registration(), a1.model())
    # print(a1.seat_plan())
    #
    # a2 = Aircraft("G-A12", "CR-J", num_rows=15, num_seats_row=4)
    # print(a2.registration(), a2.model())
    # print(a2.seat_plan())
    # pp(a2._seating)


if __name__ == '__main__':
    main()
    exit(0)