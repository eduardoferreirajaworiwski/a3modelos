import time 

import streamlit as st

from app.controllers.login_professor_controller import login

def show_login_page():
    """
    Página de login do professor
    Envia os dados para a controller validar no submit do formulário
    """

    st.header("Bem vindo ao sistema da SchoolTech!")
    st.subheader("Professor, faça login para continuar.")

    username = st.text_input("Registro acadêmico")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        res = login(username, password)
        if res:
            st.success("Login realizado com sucesso!")
            time.sleep(1) # só pra ficar bonito
            st.vm.set_page("home professor")
        
        else:
            st.error("Usuário ou senha incorretos!")
            time.sleep(1) # só pra ficar bonito