# Movie Theater Seating Challenge - 2020

Language: python

## Problem Description:
To implement an algorithm for assigning seats in a movie theatre according to the reservation requests.

###Input:
Path of an input file, provided as a command line arguement, that contains space seperated reservation identifier and number of seats requested.

The reservation identifier will have the format: R####. 

Example Input File Rows:

R0001 2 
R0002 4 
R0003 4 
R0004 3 


###Output:
The program will output the path of a file which contains reservation identifier followed by a space and then comma seperated seat numbers.

Example Output File Rows:

R0001 J1,J2 
R0002 J6,J7,J8,J9 
R0003 J13,J14,J15,J16 
R0004 H1,H2,H3


It also generates a Theatre.txt file which shows how the Theatre will look after all the reservations are done.

'-' represents an empty seat 
'*' represents a booked seat
'o' represents seats that have been left empty for customer safety


## Assumptions:

1. The buffer of 3 seats is assumed to be between each reservation and not between each seat of every Reservation. i.e if a reservation request for 4 seats comes then all the 4 seats would be given contiguosly and a buffer of 3 seats would be given between the current and next reservation.
2. The program cannot reserve seats for a group if the requested number of seats is greater than the available seats in a single row(20).
3. Customer Satisfaction: It is assumed that all the customers booking the tickets would like to sit next to each other and hence the program will  try to accomodate all seats next to each other. The second assumption is that the customers would like to have a seat far away from the screen to have a better viewing angle and hence the program will try to accomodate seats in the last rows first.


## Steps for running

1. Download and save the project folder.
2. Install pytest using the following command: 
    pip install -U pytest
3. To run with own input: 
    python driver.py 'inputFile_path'
4. To run the testcases: 
    pytest test.py
5. To view the output: 
    open the file located in the file path printed in Terminal

### Algorithm:

1. The program will first convert the Input file into a list of list with both Reservation Id and the seats requested.
2. Then it will pass the input list to our seat booking function.
3. The function will go throught the list and will first try to fill up all the even rows starting from the last row along with checking the condition of 3 seats gap between each reservation.
4. After no space is left in the even rows it will try booking seats in the odd rows.
5. Finally the program will give the output file with all the reservation ids and the seats allocated. If no seats were allocated it will assign a value of 0.
