import csv

with open('ex.csv') as csvfile:
    
    readCSV = csv.reader(csvfile, delimiter='-')
    dates = []
    colors = []
    for row in readCSV:
        print(row[0],row[1],row[2],row[3])
        dates.append(row[0])
        colors.append(row[3])

    print(dates)
    print(colors)
    try:
        whatColor = input('What color do you wish to know the date of?:')

        if whatColor in colors:
            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of',whatColor,'is:',theDate)
        else:
            print('This color was not found.')
    except Exception as e:
        print(e)
