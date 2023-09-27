import unittest
from driver import bookTickets
from seatAllocation import seatAllocation



class unitTesting(unittest.TestCase):
    
    
    #Testing the seat finder function
    def test1(self):
        total_rows = 10
        seats_per_row = 20
        theatre_layout = [['-' for i in range(seats_per_row)] for j in range(total_rows)]
        booking_list = {}
        
        row = 3  
        for i in range(0,15):
            theatre_layout[row][i] = '*'
    
        seat_alloc = seatAllocation(10, 20, theatre_layout, booking_list)      
        seat_info = seat_alloc.findSafeSeat(row)
        
                
        assert seat_info == (5,15)
    
    #Testing the funcion that provides seat numbers 
    def test2(self):
        
        total_rows = 10
        seats_per_row = 20
        theatre_layout = [['-' for i in range(seats_per_row)] for j in range(total_rows)]
        booking_list = {}
        
        row = 3  
        for i in range(0,15):
            theatre_layout[row][i] = '*'
    
        seat_alloc = seatAllocation(10, 20, theatre_layout, booking_list)
        
        booking_id = 'R0001'
        
        starting_seat = 10
        seats_required = 3
        
        seat_alloc.generateTickets(booking_id, row, starting_seat, seats_required)
        
        assert seat_alloc.booking_list[booking_id] == ['D11', 'D12', 'D13']
        
    #Testing the function for blocking reserved seats    
    def test3(self):
        
        total_rows = 10
        seats_per_row = 20
        theatre_layout = [['-' for i in range(seats_per_row)] for j in range(total_rows)]
        booking_list = {}
        
        row = 2

        seat_alloc = seatAllocation(10, 20, theatre_layout, booking_list)        
        emptySeats = (5,15)
        request = ('R0001', 3)
        
        seat_alloc.blockSeats(emptySeats, request, row)
        
        assert theatre_layout[row] == ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '*', '*', '*', 'o', 'o']
        
    def test4(self):
        
        bookTickets('../testIO/InputTestFile1.txt')
        assert [row for row in open('../testIO/OutputTestFile1.txt')] == [row for row in open('../OutputFile.txt')]
        
if __name__ == '__main__' :
    unittest.main()