import os
import tempfile
from functools import reduce
from pymongo import MongoClient
from bson import ObjectId

# Connection to MongoDB
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['students_db']
collection = db['students']


def add(student=None):
    # If student_id is not provided, generate a new ObjectId
    if not student.student_id:
        student.student_id = str(ObjectId())

    query = {"student_id": student.student_id}
    existing_student = collection.find_one(query)
    if existing_student:
        return 'already exists', 409

    result = collection.insert_one(student.to_dict())
    return student.student_id

def get_by_id(student_id=None, subject=None):
    student = collection.find_one({"student_id": student_id})
    if not student:
        return 'not found', 404
    return student

def delete(student_id=None):
    result = collection.delete_one({"student_id": student_id})
    if result.deleted_count == 0:
        return 'not found', 404
    return student_id
