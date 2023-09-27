import random

x = 0
inputFile = open("InputFile.txt", "w+")
i = 1
while x < 300:
    seatsRequested = random.randint(1, 20)
    x += seatsRequested
    inputFile.write('{} {}{}'.format("R" + '{:04d}'.format(i), seatsRequested, '\n'))
    i = i + 1

inputFile.close()
