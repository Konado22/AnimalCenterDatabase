from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user, passwd, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER=user
        PASS=passwd
        HOST=host
        PORT=port
        DB=database
        COL=collection
        ##USER = 'aacuser'
        ##PASS = 'password'
        ##HOST = 'nv-desktop-services.apporto.com'
        ##PORT = 31706
        ##DB = 'AAC'
        ##COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return self.database.animals.find_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self,data):
        if data is None:
            raise Exception("Nothing to save, because data parameter is empty")
        else:
            Readresult = self.database.animals.find(data)
            return Readresult
            
# Update Method to implement the U the CRUD
    def update(self,querry,data):
        if data:
            try:
                Updateresult= self.database.animals.update_one(querry,{'$set': data})
                print(f"Updated Entry Success")                               
            except Exception as e:
                print(f"Error during update: {e}")
                return 0
        else:
            raise Exception("Error in updating data, please check parameteres and try again")             
# Delete Method to implement the D in 
    def delete(self,data):
        if data:
            try:
                Deleteresult=self.database.animals.delete_one(data)
                print("Deleted Entry Success")  
            except Exception as e:
                print(f"Error during delete: {str(e)}")
                return 0
        else:
            raise Exception("Error in deleting data, please check parameteres and try again") 
        

          
                