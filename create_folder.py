# Import necerrsary library
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

    elif name2 != None: # If it is making the address folder it runs this 
        try: 
            os.mkdir(os.path.join(path, name1, name2))
        except OSError:  
            print ("Creation of the directory %s failed" % os.path.join(path, name1, name2))
        else:  
            print ("Successfully created the directory %s " % os.path.join(path, name1, name2))
