import os

from pymongo import MongoClient


class Database:
    def __init__(self):
        self.mongo = MongoClient(f"{os.getenv('mongo')}")

    @property
    def connections(self):
        return self.mongo.assistant

    def add_user(self, post):
        connections = self.connections
        connections.users.insert_one(post)

    def add_task(self,post):
        connections = self.connections
        connections.tasks.insert_one(post)

    def find_user(self, id):
        connections = self.connections
        data = connections.users.find_one({"_id": id})
        return data