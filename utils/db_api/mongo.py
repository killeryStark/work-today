import os

from bson.objectid import ObjectId
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

    def add_task(self, post):
        connections = self.connections
        connections.tasks.insert_one(post)

    def load_users(self):
        connections = self.connections
        return connections.users.find()

    def find_user(self, id):
        connections = self.connections
        data = connections.users.find_one({"_id": id})
        return data

    def check_task_inbox(self, id):
        connections = self.connections
        return connections.tasks.find({"user_id": id, "category": "Входящие", "done": 0})

    def check_task_today(self, id):
        connections = self.connections
        return connections.tasks.find({"user_id": id, "done": 0})

    def edit_today(self, id, param):
        connections = self.connections
        connections.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"today": param}})

    def find_task(self, id):
        connections = self.connections
        return connections.tasks.find_one({"_id": ObjectId(id)})

    def edit_tags(self, id, tags):
        connections = self.connections
        connections.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"tags": f"{tags}"}})

    def edit_done(self, id, time):
        connections = self.connections
        connections.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"done": 1, "done_time": time}})

    def add_expenses(self, id, amount, created, category_codename, base):
        connections = self.connections
        post = {
            "user_id": id,
            "amount": amount,
            "created": created,
            "category_codename": category_codename,
            "base": base
        }
        connections.expenses.insert_one(post)

    def add_notes(self, id, notes):
        connections = self.connections
        connections.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"notes": notes}})

    def add_remind(self, id, time):
        connections = self.connections
        connections.tasks.update_one({"_id": ObjectId(id)}, {"$set": {"remind": time}})

    def load_categories(self):
        connections = self.connections
        return connections.category.find()

    def check_expenses(self, id):
        connections = self.connections
        return connections.expenses.find({"user_id": id})
