import os

class fileIo:
    
    def __init__(self, total_rows, seats_per_row, theatre_layout):
        self.total_rows = total_rows
        self.seats_per_row = seats_per_row
        self.theatre_layout = theatre_layout
        return
    
    #Reads the input file and appends every booking id and seat request as a tuple into a list
    def readInput(self, inputFile):
        
        requests = []

        file = open(inputFile, 'r')
        
        for request in file:     
            request = request.split()
            requests.append([request[0], int(request[1])])
        
        file.close()
        return requests

    #Writes the final output to an output file. 
    #Also creates a layout file to show how theatre looks after bookings
    def writeOuptut(self, booking_list, booking_request):
        
        output_file = open("../OutputFile.txt", 'w+')
        

        for booking in booking_request:
            if booking[0] in booking_list:
                output_file.write('{} {}\n'.format(booking[0], ",".join(booking_list[booking[0]])))
                
            else:
                output_file.write('{} {}\n'.format(booking[0], str(0)))
            
        
        outputFilePath = os.getcwd() + '/' + 'OutputFile.txt'
        print('{} {} {}\n'.format('\n', 'Output file location:', outputFilePath))
        
        theatreFile = open("../TheatreFile.txt", 'w+')
        for row in range(self.total_rows):
            theatreFile.write(chr(row + 65) + "     ")
            for seat in range(self.seats_per_row):
                theatreFile.write(self.theatre_layout[row][seat] + " ")
            theatreFile.write('\n')
