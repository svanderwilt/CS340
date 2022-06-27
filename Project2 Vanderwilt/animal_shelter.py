from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
	""" CRUD operateions for Animal collection in MongoDB """
	def __init__(self, username, password):
		#Use MongoClient to access mongodb using credentials
		self.client = MongoClient('mongodb://%s:%s@localhost:47167/AAC' % (username, password))
		#Set database to use AAC
		self.database = self.client['AAC']

	def create(self, data):
		if data is not None:
			#attempt to create document and catch if not successful
			try:
				record = self.database.animals.insert(data)
				return True
			except Exception as e:
				print(str(e))
				return False
		#don't attempt to create record because data parameter is empty
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			return False
	
	# find documents based on any number of parameters passed in
	def read(self, parameters=None):
		#if there are parameters try to find documents and print them
		if parameters is not None:
			return self.database.animals.find(parameters,{"_id":False})

		#no parameters so find all
		else:
			return self.database.animals.find({},{"_id":False})


	""" Method that queries for and changes document(s).  
	    First input parameter is the key/value pair to find document.
	    Second input parameter is the key/value pairs to change in the document(s)"""
	def update(self, lookup, new_data):
		
		#attempt to update document and catch if not successful
		try:
			record = self.database.animals.update_many(lookup, {"$set": new_data})
			return record.raw_result
		except Exception as e:
			print("Error updating document")
			return str(e)

	""" Method that queries for and removes dcoument(s) found 
	    based on input key/value pair """
	def delete(self, data):
		if data is not None:
			try:
				result = self.database.animals.delete_many(data)
				return result.raw_result
			except Exception as e:
				return str(e)
	