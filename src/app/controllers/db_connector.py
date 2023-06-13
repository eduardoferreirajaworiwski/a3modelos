"""
Módulo responsável por conectar com o banco de dados, outros módulos importam o db deste módulo.
"""


from pymongo import MongoClient

client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]