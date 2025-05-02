# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create or access a database
db = client["my_database"]

# Create or access a collection
collection = db["my_collection"]
# Insert a single document
collection.insert_one({"name": "Alice", "age": 25, "city": "New York"})

# Insert multiple documents
collection.insert_many([
    {"name": "Bob", "age": 30, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"}
])
# Find one document
print(collection.find_one({"name": "Alice"}))

# Find all documents
for doc in collection.find():
    print(doc)
# Update a single document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

# Update multiple documents
collection.update_many({"city": "London"}, {"$set": {"country": "UK"}})
# Delete a single document
collection.delete_one({"name": "Charlie"})

# Delete multiple documents
collection.delete_many({"city": "Paris"})
