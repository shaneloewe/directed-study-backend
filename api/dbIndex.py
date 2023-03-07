# Get the database using the method we defined in pymongo_test_insert file
from dbGet import get_database
wenevrdb = get_database()

# Create a new collection
users = wenevrdb["users"]

# Create an index on the collection
category_index = users.create_index("category")
