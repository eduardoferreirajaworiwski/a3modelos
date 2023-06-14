import streamlit as st

from app.views.professor_commons import sidebar_professor
from app.models.conteudos import get_conteudos, update_conteudo, delete_conteudo
from app.models.subjects import get_subject_names


def conteudos_edit_page():
    """
    Página para editar conteúdos

    Busca conteúdos já existentes e permite editar ou excluir através de um formulário e uma selectbox para selecionar o conteúdo a ser editado/excluído
    """
    sidebar_professor()

    conteudos = get_conteudos()
    conteudos = [conteudo for conteudo in conteudos]

    st.header("Editar e deletar conteúdos")

    opcoes = ["Selecionar"]
    opcoes.extend(
        [f'{conteudo["date"]} - {conteudo["content_name"]}' for conteudo in conteudos]
    )

    selected_option = st.selectbox("Selecione um conteúdo para editar", opcoes)

    if selected_option != "Selecionar":
        conteudo = conteudos[opcoes.index(selected_option) - 1]
        with st.form(key="edit_conteudo"):
            new_name = st.text_input("Nome", conteudo["content_name"])
            new_subject = st.selectbox(
                "Matéria",
                get_subject_names(),
                index=get_subject_names().index(conteudo["subject"]),
            )
            new_description = st.text_input("Descrição", conteudo["description"])

            new_data = {
                "content_name": new_name,
                "subject": new_subject,
                "description": new_description,
            }

            cols = st.columns(2, gap="large")

            with cols[0]:
                if st.form_submit_button("Editar"):
                    update_conteudo(
                        {
                            "content_name": conteudo["content_name"],
                            "date": conteudo["date"],
                        },
                        new_data,
                    )
                    st.success("Conteúdo editado com sucesso!")

            with cols[1]:
                if st.form_submit_button("Deletar"):
                    delete_conteudo(
                        {
                            "content_name": conteudo["content_name"],
                            "date": conteudo["date"],
                        }
                    )
                    st.success("Conteúdo deletado com sucesso!")
