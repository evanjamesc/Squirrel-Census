# Library imports
import pandas  # Pandas for data manipulation
from pymongo import MongoClient  # Pymongo for MongoDB integration

# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://evanjameschristianson:qKC9nT8B66pegcwj@cluster0.vef0yha.mongodb.net/?retryWrites=true&w=majority")
db = client["squirrel_database"]  # Connect to the 'squirrel_database' database
collection = db["squirrel_counts"]  # Connect to the 'squirrel_counts' collection

# Read CSV data using pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Calculate squirrel counts by fur color
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])  # Count of gray squirrels
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])  # Count of cinnamon (red) squirrels
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])  # Count of black squirrels

# Prepare data for CSV and MongoDB as key-value pairs in a dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],  # Fur colors
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]  # Corresponding counts
}

# Create Pandas DataFrame from the dictionary and save to CSV
df = pandas.DataFrame(data_dict)  # Creating a DataFrame from the dictionary
df.to_csv("squirrel_count.csv")  # Saving the DataFrame to a CSV file

# Print counts to the console for checking accuracy
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# Insert data into MongoDB
collection.insert_one(data_dict)  # Insert the data dictionary as a document into MongoDB
