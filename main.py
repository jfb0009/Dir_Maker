# Import necessary libraries

from create_folder import create_folder
import csv


def main():
    path = "C:\\Users\\Jose Garcia\\Desktop\\Total Fire Protection"     # The path for the cities folders to be made
    cities = []                                                         # The list for the cities names
    addresses = []                                                      # The list for the address folders already created

    # Opens the csv and reads it into a list 
    with open("Competitor_Drawing_Sorted.csv") as file:     
        fl = list(csv.reader(file))

    # For every line it takes off any trailing spaces on the cities and appends them to the list only once
    for line in fl:
        if line[1].rstrip() not in cities and line[1] != '': # Appends all of the cities to the cities list only once
            cities.append(line[1].rstrip())

    # Makes a folder for each city
    for city in cities:
        create_folder(path, city)
        
    # For every sublist it checks if the address has already been made if not it finds the city it goes in and makes a folder
    # It then appends the address to the lsit of created folders
    for line in fl:
        for city in cities:
            if (line[0] not in addresses) and (city == line[1].rstrip()) and (line[0].rstrip() != ''):
                create_folder(path, city, line[0])
            
        addresses.append(line[0])
        

    return


# Runs the file
if __name__ == "__main__":
    main()