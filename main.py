# Import necessary libraries

import os
import csv


def create_folder(path, name1, name2 = None):
# Function to take in a path and the names of the folders it has to create

    if name2 == None: # If it is just making the cities folder it runs this one
        try: 
            os.mkdir(os.path.join(path, name1))
        except OSError:  
            print ("Creation of the directory %s failed" % os.path.join(path, name1))
        else:  
            print ("Successfully created the directory %s " % os.path.join(path, name1))

    else: # If it is making the cities folder it uses this one
        try: 
            os.mkdir(os.path.join(path, name1, name2))
        except OSError:  
            print ("Creation of the directory %s failed" % os.path.join(path, name1, name2))
        else:  
            print ("Successfully created the directory %s " % os.path.join(path, name1, name2))



def main():
    path = "C:\\Users\\Jose Garcia\\Desktop\\Total"     # The path for the cities folders to be made
    cities = []                                         # The list for the cities names
    addresses = []                                      # The list for the address folders already created


    with open("Competitor_Drawing_Sorted.csv") as file:     
        fl = csv.reader(file)

    
        for line in fl:
            if line[1] not in cities and line[1] != '': # Appends all of the cities to the cities list only once
                cities.append(line[1])


        unique_cities = set(cities)
        for city in unique_cities:
            city.strip()
            create_folder(path, city)
        

        """ for line in fl:
            for city in cities:
                if line[0] not in addresses and city == line[1] and line[0] != '':
                    create_folder(path, city.strip(), line[0].strip())
            
            addresses.append(line[0]) """
        
    return


# Runs the file
if __name__ == "__main__":
    main()