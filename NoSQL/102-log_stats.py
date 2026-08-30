#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
PIPE = [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}, {"$limit": 10}]


def log_stats(mongo_collection):
    """ script that provides some stats about Nginx logs stored in MongoDB
    """
    total = mongo_collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
    print("IPs:")
    for ip in mongo_collection.aggregate(PIPE):
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == "__main__":
    log_stats(MongoClient('mongodb://127.0.0.1:27017').logs.nginx)
