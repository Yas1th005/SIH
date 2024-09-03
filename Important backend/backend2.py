from pymongo import MongoClient
import requests

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['sih-data']
collection = db['news']

# Function to fetch API data
def fetch_api_data():
    api_url = 'http://localhost:5000/news'  # Replace with your API endpoint
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch data')
        return None

# Function to insert data into MongoDB
def insert_data_into_mongodb(data):
    if data:
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)
        print('Data inserted successfully')
    else:
        print('No data to insert')

# Fetch and insert data
api_data = fetch_api_data()
insert_data_into_mongodb(api_data)
