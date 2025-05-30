from pymongo import MongoClient
import os
# Optional: Default/fallback URI for development
DEFAULT_MONGODB_URI = "mongodb+srv://Govind_Singh_Rajput:zyxw@cluster0.iywwlbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Load environment variables
MONGODB_URI = os.getenv("MONGODB_URI", DEFAULT_MONGODB_URI)
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "UserData")

# Attempt to connect
try:
    if MONGODB_URI:
        client = MongoClient(MONGODB_URI)
        db = client[MONGODB_DATABASE]
        responses_collection = db["responses"]
        print(f"Connected to MongoDB database: {MONGODB_DATABASE}")
    else:
        responses_collection = None
        print(" MONGODB_URI not set; responses will not be saved in MongoDB.")
except Exception as e:
    responses_collection = None
    print(f"Failed to connect to MongoDB: {e}")
