import streamlit as st
from streamlit_option_menu import option_menu

def home_preauth():
    """
    Página inicial do sistema.
    Aparece quando você não está logado, e te dá a opção de logar como aluno ou professor.
    Chama a função set_page do ViewManager quando você seleciona uma opção.
    """
    st.title("Bem-vindo ao sistema da SchoolTech!")
    navbar_options = ["Selecione a opção", "Aluno", "Professor"]
    selected_option = option_menu("Você é aluno ou professor?", navbar_options)

    if selected_option and selected_option != "Selecione a opção":
        page_mapping = {"Aluno": 'login aluno', "Professor": "login professor"}
        page_name = page_mapping[selected_option]

        if page_name:
            st.vm.set_page(page_name)