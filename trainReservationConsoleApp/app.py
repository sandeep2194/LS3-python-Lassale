import csv
import random

trainsCSVFile = "trains.csv"
reservationsCSVFile = "reservations.csv"


def writeAFile(fileName, row=[], rows=[], fields=[], mode='a'):
    with open(fileName, mode) as csvfile:
        csvwriter = csv.writer(csvfile)
        if (mode == 'w'):
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        else:
            csvwriter.writerow(row)


def readAFile(fileName):
    rows = []

    with open(fileName, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            rows.append(row)
    return rows


def askUser():
    print("Press 1 to Search Trains from station a to b and genrate a ticket")
    print("Press 2 to cancel a Ticket")
    selection = input("Choose from options above: ")
    return selection


def createTicket(trainNo, date, fromStation, toStation, noOfPasengers, price
                 ):
    ticketNumber = random.randint(100000, 1000000)
    totalPrice = noOfPasengers*price
    row = [ticketNumber, trainNo, date, fromStation,
           toStation, noOfPasengers, totalPrice]

    writeAFile(reservationsCSVFile, row)

    return "Reservation Succesfully Created with ticket number: " + str(ticketNumber)


def cancelAReservation(ticketNumber):
    rows = readAFile(reservationsCSVFile)
    fields = rows[0]
    newRows = []
    for row in rows:
        if (row[0] != str(ticketNumber)):
            newRows.append(row)
    newRows.remove(fields)
    if (len(newRows) > 0):
        writeAFile(reservationsCSVFile, [], newRows, fields, 'w')
        return "Ticket cancelled successfully"
    return "Ticket Not Found"


def searchTrains(station_a, station_b):
    rows = readAFile(trainsCSVFile)
    trains = []

    for row in rows:
        a = row[1]
        b = row[2]
        if (station_a == a and station_b == b):
            trains.append(row)

    return trains


userSelection = askUser()
selectedTrain = []
if userSelection == '1':
    station_a = input('Enter from which station you want to start? : ')
    station_b = input('Enter to which station you want to go? : ')
    avaibleTrains = searchTrains(station_a, station_b)
    print(
        f'Trains from {station_a} to {station_b} are : ')
    for train in avaibleTrains:
        print(
            f'{avaibleTrains.index(train)+1}) trainNo: {train[0]},fromStation: {train[1]},toStation: {train[2]},seats: {train[3]},price: {train[4]}')
    rowSelected = input(
        'Type train row no. to Select a train for genrating a ticket: ')
    selectedTrain = avaibleTrains[int(rowSelected)-1]
    date = input('what is date of journey? : ')
    noofPasengers = input('how many people are going? : ')
    tickNum = createTicket(
        selectedTrain[0], date, selectedTrain[1], selectedTrain[2], int(noofPasengers), selectedTrain[4])
    print(tickNum)
elif userSelection == '2':
    tNo = input('What is the ticket number for cancellation? : ')
    cancellation = cancelAReservation(tNo)
    print(cancellation)
