"""
A Flight Class.  Model for aircraft flights
"""


class Flight:
    """
    A flight with a particular passenger aircraft
    """
    # define our initializer (in other languages this is a constructor)
    def __init__(self, number, aircraft):
        # if variable begins with one underscore its a private variable
        # this is a common convention for Python
        # Implementation details begin with "_"
        # We need to confirm our Flight is AA###
        if len(number) != 5:
            raise ValueError("Invalid flight number length {}".format(number))
        if not number[2:].isnumeric():
            raise ValueError('Flight number must end with three numeric digits {}'.format(number))
        if not number[:2].isalpha():
            raise ValueError('Flight number must start with 2-character Airline Code {}'.format(number))
        if not number[:2].isupper():
            raise ValueError('Airline Code must be capitalized {}'.format(number))
        self._number = number
        # Add aicraft as another parameter
        self._aircraft = aircraft
        rows, seats = self._aircraft.seat_plan()
        self._seating = [None] + \
                        [{letter: None for letter in seats} for _ in rows]


    def allocate_seat(self, seat, passenger):
        """
        Allocate a seat for the passenger
        :param seat: seat designator (such as '12C', '21F'
        :param passenger: Passenger name (such as 'Jane Doe')
        :return:
        """
        rows, seat_letter = self._aircraft.seat_plan()
        letter = seat[-1]      # take the letter from the seat
        if letter not in seat_letter:
            raise ValueError('Invalid seat letter {}'.format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError('Invalid row {}'.format(row_text))
        if row not in rows:
            raise ValueError('Invalid row number {}'.format(row))
        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} already occupied '.format(seat))
        #Assign the seat
        self._seating[row][letter] = passenger



        pass


    def airline(self):
        """
        Convert the Flight number into an Airline Code
        :return: Return the Airline Code portion of the Flight number
        """
        # code = self._number[:2]    => Didn't quite understand what was being asked for => Corrected below
        # if code == 'DL':
        #     return 'Delta Airlines'
        # if code == 'AM':
        #     return 'American Airlines'
        # if code == 'SW':
        #     return 'Southwest Airlines'
        # if code == 'UN':
        #     return 'United Airlines'
        # return 'Invalid airline code'
        return self._number[:2]

    def number(self):
        """"
        Convert the flight number into just the flight numeric digits
        :return: flight number (3 digits)
        """
        return self._number[2:]


class Aircraft:
    """
    Create a class that defines an aircraft
    """
    def __init__(self, registration, model, num_rows, num_seats_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_row = num_seats_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seat_plan(self):
        """
        Create tuple for the seat_plan that contains seats: A, B, C, D, E, F, G, H, J, K
        :return: A tuple of the row number with the seat (row, seats)
        """
        return(range(1, self._num_rows +1), 'ABCDEFGHJK'[:self._num_seats_row])




def main():
    """
    test function
    :return: nothing
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)