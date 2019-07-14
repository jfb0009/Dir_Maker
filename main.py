# Import necessary libraries

import os


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
    cities = []                                     # The list for the cities names
    addresses = []                                  # The list for the address folders already created

    with open("Competitor_Drawing_Sorted.csv") as file:     
        fl = file.readlines()
        fl.pop(0)
        for line in fl:
            # For every lin in the list of the file it creates a list of the strings and saves that to the lines spot
            fl[fl.index(line)] = line.split(',')



    for line in fl: # For all the lists in the list if that city isnt added it adds it to the list of cities
        if line[3] not in cities:
            cities.append(line[3])


    for i in range(5):
        create_folder(path, cities[i])

    return


# Runs the file
if __name__ == "__main__":
    main()