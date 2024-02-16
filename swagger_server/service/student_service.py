import os
import tempfile
from functools import reduce
from pymongo import MongoClient

# Connection to MongoDB
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['students_db']
collection = db['students']

def add(student=None):
    queries = []
    query = {"first_name": student.first_name, "last_name": student.last_name}
    res = collection.find_one(query)
    if res:
        return 'already exists', 409

    result = collection.insert_one(student.to_dict())
    student.student_id = str(result.inserted_id)
    return student.student_id

def get_by_id(student_id=None, subject=None):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        return 'not found', 404
    student['student_id'] = student_id
    print(student)
    return student

def delete(student_id=None):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        return 'not found', 404
    collection.delete_one({"_id": ObjectId(student_id)})
    return student_id
