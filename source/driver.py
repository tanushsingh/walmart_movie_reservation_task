import sys
from fileIo import fileIo
from seatAllocation import seatAllocation

#Driver code for booking movie tickets
def bookTickets(file):
    
    total_rows = 10
    seats_per_row = 20
    #Creating an empty theatre layout
    theatre_layout = [['-' for i in range(seats_per_row)] for j in range(total_rows)]
    booking_list = {}
    
    f_io = fileIo(total_rows, seats_per_row, theatre_layout)
    seat_alloc = seatAllocation(total_rows, seats_per_row, theatre_layout, booking_list)

    
    booking_requests = f_io.readInput(file)
    booking_list = seat_alloc.reserveSeats(booking_requests)
    
    
    f_io.writeOuptut(booking_list, booking_requests)


if __name__ == '__main__':

    try:
        filePath = sys.argv[1]
        bookTickets(filePath)
    except FileNotFoundError:
        print('!!!Input file not found!!!')
        # filePath = '../InputFile.txt'
        # bookTickets(filePath)
        
    
