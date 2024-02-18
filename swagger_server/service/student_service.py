import os
import tempfile
from functools import reduce
from pymongo import MongoClient

# Connection to MongoDB
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
# client = MongoClient(mongo_uri)
# db = client['students_db']
# collection = db['students']


def add(student=None):
    print('Connecting to MongoDB at', mongo_uri)
    client = MongoClient(mongo_uri)
    db = client['students_db']
    collection = db['students']
    result = collection.insert_one(student.to_dict())
    return student.student_id
    # return 'already exists', 409
    # # If student_id is not provided, generate a new unique id
    # if not student.student_id:
    #     # Find the maximum student_id and increment it by 1
    #     max_student_id = collection.find_one({}, sort=[("student_id", -1)])
    #     new_student_id = int(max_student_id.get('student_id', 0)) + 1
    #     student.student_id = new_student_id
    #
    # query = {"student_id": student.student_id}
    # existing_student = collection.find_one(query)
    # if existing_student:
    #     return 'already exists', 409
    #
    # result = collection.insert_one(student.to_dict())
    # return student.student_id

# def get_by_id(student_id=None, subject=None):
#     student = collection.find_one({"student_id": student_id}, {'_id': False})
#     if not student:
#         return 'not found', 404
#     return student
#
# def delete(student_id=None):
#     result = collection.delete_one({"student_id": student_id})
#     if result.deleted_count == 0:
#         return 'not found', 404
#     return student_id
