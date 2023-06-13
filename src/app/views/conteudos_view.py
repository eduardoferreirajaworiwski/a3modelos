import streamlit as st

from app.views.professor_commons import sidebar_professor

from app.models.conteudos import get_conteudos

def conteudos_view_page():
    """
    Página para visualizar conteúdos
    """

    sidebar_professor()
    st.title("Visualizar Conteúdos")

    conteudos = get_conteudos()
    for conteudo in conteudos:
        with st.expander(f'{conteudo["date"]} - {conteudo["content_name"]}'):
            st.markdown(f"Matéria: ```{conteudo['subject']}```")
            st.markdown(f"Descrição: ```{conteudo['description']}```")