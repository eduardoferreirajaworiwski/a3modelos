"""
Model responsável por fazer a conexão com o banco de dados e realizar as operações relacionadas a disciplinas
"""


from app.controllers.db_connector import db

collection_subjects = db["subjects"]

def get_subject_names():
    subjects = collection_subjects.find({}, {"name": 1})
    subject_names = [subject["name"] for subject in subjects]
    return subject_names

def create_subject(name):
    if name:
        subject_data = {
            "name": name,
        }
        collection_subjects.insert_one(subject_data)
        return True
    return False