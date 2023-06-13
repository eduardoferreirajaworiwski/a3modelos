"""
Model responsável por fazer a conexão com o banco de dados e realizar as operações de login
"""


from app.controllers.db_connector import db

users_collection = db["users"]

def login_professor(username, password):
    professor = users_collection.find_one({"username": username, "password": password}) #, 'type': 'professor'})
    return professor if professor else None

def login_aluno(username, password):
    aluno = users_collection.find_one({"username": username, "password": password}) #, 'type': 'aluno'})
    return aluno if aluno else None