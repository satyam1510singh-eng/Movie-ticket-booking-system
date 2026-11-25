# Movie Ticket Booking System
# Project No.: 47
# Concepts: 2D Lists, Seat Management, Functions, and File Handling

# ----------------------------- CONSTANTS -----------------------------

ROWS = ["A", "B", "C"]
SEAT_NUMBERS = [1, 2, 3, 4, 5]
TICKET_PRICE = 200
BOOKING_FILE = "bookings.txt"

# The seat map is stored as a 2D list with 3 rows and 5 seats per row.
# None means the seat is available.
# A customer name means the seat is booked.
# Example: seat_map[0][0] = "Aman" means seat A1 is booked by Aman.
seat_map = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]


# -------------------------- SEAT VALIDATION ----------------------------

def is_valid_seat(seat):
    """Return True if the seat is between A1 and C5."""
    seat = seat.strip().upper()

    if len(seat) != 2:
        return False

    row = seat[0]
    number = seat[1]

    if row in ROWS and number in ["1", "2", "3", "4", "5"]:
        return True

    return False


def get_seat_position(seat):
    """Convert a seat label such as B3 into 2D-list indexes."""
    row_index = ROWS.index(seat[0])
    seat_index = int(seat[1]) - 1
    return row_index, seat_index


# -------------------------- FILE HANDLING ------------------------------

def load_bookings():
    """Load previously saved bookings into the 2D seat map."""
    global seat_map

    # Start with all seats available.
    seat_map = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]

    # Create bookings.txt if it does not already exist.
    file = open(BOOKING_FILE, "a")
    file.close()

    file = open(BOOKING_FILE, "r")

    for line in file:
        line = line.strip()

        if line != "" and "," in line:
            seat, name = line.split(",", 1)
            seat = seat.strip().upper()
            name = name.strip()

            if is_valid_seat(seat) and name != "":
                row_index, seat_index = get_seat_position(seat)
                seat_map[row_index][seat_index] = name

    file.close()


def save_bookings():
    """Save every booked seat and customer name into bookings.txt."""
    file = open(BOOKING_FILE, "w")

    for row_index in range(len(ROWS)):
        for seat_index in range(len(SEAT_NUMBERS)):
            customer_name = seat_map[row_index][seat_index]

            if customer_name is not None:
                seat = ROWS[row_index] + str(seat_index + 1)
                file.write(seat + "," + customer_name + "\n")

    file.close()


# --------------------------- SEAT DETAILS -------------------------------

def count_available_seats():
    """Count the seats whose values are None in the 2D list."""
    available = 0

    for row in seat_map:
        for customer_name in row:
            if customer_name is None:
                available += 1

    return available


def display_seat_map():
    """Display X for booked seats and _ for available seats."""
    print("\n             SEAT MAP")
    #print("       1   2   3   4   5")

    for row_index in range(len(ROWS)):
        print("Row " + ROWS[row_index] + ": ", end="")

        for seat_index in range(len(SEAT_NUMBERS)):
            if seat_map[row_index][seat_index] is not None:
                print(" X  ", end="")
            else:
                print(" _  ", end="")

        print()

    print("Seats left:", count_available_seats())

    if count_available_seats() == 0:
        print("Show is now housefull.")


# ---------------------------- BOOK A SEAT -------------------------------

def book_seat():
    """Book one or more available seats for a customer."""
    seat_input = input("Seat: ").strip().upper()

    # Accept one seat (A1) or multiple comma-separated seats (A2,A3).
    seats = [seat.strip() for seat in seat_input.split(",")]

    # Validate all requested seats before changing the seat map.
    for seat in seats:
        if not is_valid_seat(seat):
            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            return

    # Prevent the same seat from being entered more than once.
    if len(seats) != len(set(seats)):
        print("Duplicate seat entered. Please enter each seat only once.")
        return

    # Check whether any requested seat is already booked.
    for seat in seats:
        row_index, seat_index = get_seat_position(seat)

        if seat_map[row_index][seat_index] is not None:
            print("Seat " + seat + " is already booked.")
            return

    name = input("Name: ").strip()

    if name == "":
        print("Invalid customer name. Name cannot be empty.")
        return

    # Book all requested seats for the same customer.
    for seat in seats:
        row_index, seat_index = get_seat_position(seat)
        seat_map[row_index][seat_index] = name

    save_bookings()

    amount = len(seats) * TICKET_PRICE

    if len(seats) == 1:
        print("Seat " + seats[0] + " booked for " + name + ". Amount: " + str(amount))
    else:
        print("Seats " + ", ".join(seats) + " booked for " + name + ". Amount: " + str(amount))

    if count_available_seats() == 0:
        print("Seats left: 0")
        print("Show is now housefull.")


# -------------------------- CANCEL A BOOKING ----------------------------

def cancel_booking():
    """Cancel a booking by entering its seat number."""
    seat = input("Seat to cancel: ").strip().upper()

    if not is_valid_seat(seat):
        print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
        return

    row_index, seat_index = get_seat_position(seat)

    if seat_map[row_index][seat_index] is None:
        print("Seat " + seat + " is not booked.")
        return

    customer_name = seat_map[row_index][seat_index]
    seat_map[row_index][seat_index] = None
    save_bookings()

    print("Booking for seat " + seat + " (" + customer_name + ") cancelled successfully.")
    print("Seats left:", count_available_seats())


# ----------------------------- MAIN MENU --------------------------------

def display_menu():
    """Display the application menu."""
    print("\n========== MOVIE TICKET BOOKING SYSTEM ==========")
    print("1. Book")
    print("2. Cancel")
    print("3. Seat map")
    print("4. Exit")


def main():
    """Run the movie ticket booking application."""
    load_bookings()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_seat()

        elif choice == "2":
            cancel_booking()

        elif choice == "3":
            display_seat_map()

        elif choice == "4":
            print("Thank you for using the Movie Ticket Booking System.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# Start the application.
# In Jupyter Notebook, call main() directly when this cell runs.
main()

    