#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx
    print(db.count_documents({}), "logs\nMethods:")
    print("\tmethod GET:", db.count_documents({"method": "GET"}))
    print("\tmethod POST:", db.count_documents({"method": "POST"}))
    print("\tmethod PUT:", db.count_documents({"method": "PUT"}))
    print("\tmethod PATCH:", db.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE:", db.count_documents({"method": "DELETE"}))
    print(db.count_documents({"method": "GET", "path": "/status"}), "status check")
    client.close()
