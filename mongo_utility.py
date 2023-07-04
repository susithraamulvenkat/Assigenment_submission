from scripts.core.db.mongodb import Mongodb

mongodb = Mongodb()
collection_one = mongodb.connect_collection('susithra_db2')
collection_two = mongodb.connect_collection('susithra_db3')
collection_three = mongodb.connect_collection('susithra_db4')
collection_four = mongodb.connect_collection('susithra_db5')
