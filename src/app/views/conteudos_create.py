
import streamlit as st

from app.views.professor_commons import sidebar_professor
from app.models.conteudos import create_conteudo
from app.models.subjects import get_subject_names

def conteudos_create_page():
    """
    View para cadastro de conteúdos.
    """
    sidebar_professor()
    st.title("Cadastro de Conteúdo")
    content_name = st.text_input("Nome do Conteúdo")
    selected_subject = st.selectbox("Matéria", get_subject_names())
    date = st.date_input("Data de Cadastro")
    description = st.text_area("Descrição do Conteúdo", height=200)
    if st.button("Cadastrar"):
        print(f'Novo conteúdo: {content_name} - {selected_subject} - {date} - {description}')
        data = {
            "content_name": content_name,
            "subject": selected_subject,
            "date": date.strftime("%d-%m-%Y"),
            "description": description,
        }
        res = create_conteudo(data)
        if res:
            st.success("Conteúdo cadastrado com sucesso!")
        else:
            st.error("Erro ao cadastrar conteúdo.")
