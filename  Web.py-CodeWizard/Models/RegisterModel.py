import pymongo
from pymongo import MongoClient
import bcrypt, os

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.pytest
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.Users.insert({
            "username": data.username,
            "name": data.name,
            "password": data.password,
            "email": data.email,
            "avatar": "",
            "background": "",
            "about": "",
            "hobies": "",
            "birtday": ""
        })
        print("uid is", id)
        myuser = self.Users.find_one({"username": data.username})

        if bcrypt.checkpw("avocadol".enencode(), myuser["password"]):
            print("this matches")