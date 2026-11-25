# Movie Ticket Booking System

## Project Details

- **Project Title:** Movie Ticket Booking System
- **PS No.:** 47
- **Name:** Satyam Kumar Singh
- **ERP:** 02090
- **Email:** satyam.kumar.singh3@rungta.org
- **Section:** BCA 1C

---

## Project Overview

The **Movie Ticket Booking System** is a menu-driven Python application that allows users to book movie seats, cancel existing bookings, and view the current seat map. It uses a 2D list to manage seats and a text file to save booking information so that bookings remain available when the program is started again.

## Features

1. **Book Seats:** Book one seat or multiple seats for a customer.
2. **Cancel Booking:** Cancel a booking by entering the seat number.
3. **View Seat Map:** Display booked and available seats.
4. **Available Seat Count:** Show how many seats are still available.
5. **Booking Validation:** Check seat labels, prevent duplicate seat entries, and stop users from booking an already-booked seat.
6. **File Handling:** Save bookings in `bookings.txt` and load them when the application starts.
7. **Housefull Message:** Display a message when all seats have been booked.

## Seat Layout and Ticket Price

- **Rows:** A, B, and C
- **Seats per row:** 5
- **Total seats:** 15
- **Ticket price:** ₹200 per seat

| Row | Seat Numbers |
|---|---|
| A | A1, A2, A3, A4, A5 |
| B | B1, B2, B3, B4, B5 |
| C | C1, C2, C3, C4, C5 |

In the seat map:
- `X` represents a booked seat.
- `_` represents an available seat.

## Technologies and Concepts Used

- Python
- 2D Lists
- Functions
- Conditional Statements
- Loops
- Input Validation
- File Handling
- String Operations

## Requirements

- Python 3.x
- A terminal or command prompt to run the program

No external Python packages are required.

## How to Run

1. Keep the Python source file (for example, `one.py`) in your project folder.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python one.py
   ```

4. Follow the on-screen menu.

## Main Menu

When the program starts, it displays these options:

```text
========== MOVIE TICKET BOOKING SYSTEM ==========
1. Book
2. Cancel
3. Seat map
4. Exit
```

- Enter `1` to book one or more seats.
- Enter `2` to cancel a booking.
- Enter `3` to display the seat map and available seat count.
- Enter `4` to exit the application.

## Data Storage

The application stores booking information in a file named `bookings.txt`. Each saved booking is stored as a seat number followed by the customer name, separated by a comma.

Example:

```text
A1,Satyam
B3,Rahul
```

The program loads this file when it starts and updates it after a booking or cancellation.

## Project Structure

```text
Movie-Ticket-Booking-System/
├── one.py
├── README.md
└── bookings.txt   # Created automatically when the program runs
```

## Conclusion

The Movie Ticket Booking System demonstrates how Python functions, 2D lists, validation, and file handling can be combined to create a simple seat-booking application. It provides basic booking, cancellation, and seat-availability features through a menu-driven interface.
