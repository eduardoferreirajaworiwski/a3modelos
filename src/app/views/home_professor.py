import streamlit as st

from app.views.professor_commons import sidebar_professor

def show_welcome_message():
    """
    Placeholder para a página inicial do professor, só manda usar a sidebar.
    """

    st.header("Bem-vindo professor!")
    st.subheader('Selecione uma opção no menu lateral para começar.')


def home_professor():
    """
    Página inicial do professor, não tem nada mas redireciona para as outras páginas através da sidebar.
    """

    show_welcome_message()
    sidebar_professor()