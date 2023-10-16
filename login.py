from pymongo import MongoClient
import hashlib

def check_user_exists(username, password):
    client = MongoClient("mongodb://test:sparta@ac-tcz4ypm-shard-00-00.jrmp0f9.mongodb.net:27017,ac-tcz4ypm-shard-00-01.jrmp0f9.mongodb.net:27017,ac-tcz4ypm-shard-00-02.jrmp0f9.mongodb.net:27017/?ssl=true&replicaSet=atlas-cjylmf-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.login
    collection = db.mylogin

    user = collection.find_one({"username": username, "password": password})

    if user:
        return True
    else:
        return False

username = input("Enter your username: ")
password = input("Enter your password: ")

if check_user_exists(username, password):
    print("Login successful")
else:
    print("Invalid username or password")


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

username = input("Enter your username: ")
password = input("Enter your password: ")
hashed_password = hash_password(password)

if check_user_exists(username, hashed_password):
    print("Login successful")
else:
    print("Invalid username or password")