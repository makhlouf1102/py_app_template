from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load env variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("DB_LINK"))

# database
db = client['MoneySpy']

# gettting collection
collection_users = db['users']


