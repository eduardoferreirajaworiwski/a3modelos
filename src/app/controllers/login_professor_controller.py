"""
Controller para o login do professor
Valida os dados antes de enviar para o model que faz a conexão com o banco de dados
"""


from app.models.users import login_professor

def login(username, password):
    try:
        if int(username):
            return login_professor(username, password)
        
    except ValueError: # caso a matricula não seja um número
        return None