# '-' represents empty seats, '*' represents booked seats 
# and 'o' represents seats left empty for customer safety

class seatAllocation:
    
    def __init__(self, total_rows, seats_per_row, theatre_layout, booking_list):
        
        self.total_rows = total_rows
        self.seats_per_row = seats_per_row
        self.theatre_layout = theatre_layout
        self.booking_list = booking_list
        # self.safe_rows = [1,3,5,7,9]
        
    #Finds the available seats ensuring customer safety
    def findSafeSeat(self, row):
        
        return (self.theatre_layout[row].count('-'), self.theatre_layout[row].index('-')) if '-' in self.theatre_layout[row] else (0, 0)
    
    #Finding seats previously avoided due to customer safety
    def findSeat(self, row):
        
        return (self.theatre_layout[row].count('o'), self.theatre_layout[row].index('o')) if 'o' in self.theatre_layout[row] else (0, 0)

    #Stores seats for a booking request in a dictionary
    def generateTickets(self, booking_id, row, starting_seat, seats_required):
        row_name = chr(row + 65)
        self.booking_list[booking_id] = []
        for seat in range(starting_seat, starting_seat + seats_required):
            self.booking_list[booking_id].append(row_name +str(seat+1))

    #Marks seats as reserved, so they are not booked again
    def blockSeats(self, emptySeats, request, row):
        booking_id = request[0]
        seats_required = request[1]
        starting_seat = emptySeats[1]
        
        #Book required seats
        for seat in range(starting_seat, starting_seat + seats_required):
            self.theatre_layout[row][seat] = '*'
        
        #Block seats for safety
        #3 adjacent seats
        blocked_seat = starting_seat + seats_required
        for seat in range(blocked_seat, blocked_seat + 3):
            if seat >= self.seats_per_row:
                break
            if self.theatre_layout[row][seat] != '*':
                self.theatre_layout[row][seat] = 'o'
        
        #adjacent row
        next_row = row - 1
        if next_row >= 0 and next_row%2 != 0:
            for seat in range(self.seats_per_row):
                if self.theatre_layout[next_row][seat] != '*' :
                    self.theatre_layout[next_row][seat] = 'o'
        
        self.generateTickets(booking_id, row, starting_seat, seats_required)
        
        return True
            
        
    #Code that handles all the reservation of seats, marking them as booked and keeping them in the dictionary
    def reserveSeats(self, requests):
        
        for request in requests:
            booking_successful = False
            print(request)
            #Trying to find seats in alternate rows
            for row in range(self.total_rows - 1, -1, -2):
                emptySeats = self.findSafeSeat(row)
                print("Printing empty seats for row", row, emptySeats)
                if emptySeats[0] >= request[1]:
                    booking_successful = self.blockSeats(emptySeats, request, row)
                    break
  
            if booking_successful == True:
                continue
            
            #If seats are not available in alternate rows, we try to find seats in adjacent rows
            for row in range(self.total_rows - 2, -1, -2):
                emptySeats = self.findSeat(row)
                print("Printing unsafe seats for row", row, emptySeats)
                if emptySeats[0] >= request[1]:
                    self.blockSeats(emptySeats, request, row)
                    break
            
        return self.booking_list