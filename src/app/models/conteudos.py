"""
Model responsável por fazer a conexão com o banco de dados e realizar as operações relacionadas a conteúdos, como criar, buscar e atualizar
"""


from app.controllers.db_connector import db
    
collection_conteudos = db["conteudos"]

def get_conteudos(subject=None):
    if subject:
        conteudos = collection_conteudos.find({"subject": subject})
    else:
        conteudos = collection_conteudos.find({})
    return conteudos

def update_conteudo(filtro, data):
    collection_conteudos.update_one(filtro, {"$set": data})
    return True

def create_conteudo(data):
    collection_conteudos.insert_one(data)
    return True