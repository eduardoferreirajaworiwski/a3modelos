import streamlit as st

def sidebar_professor():
    """
    Sidebar usada em todas as páginas do professor.
    Chama o set_page do ViewManager quando o botão é clicado.
    """

    page_mapping = {
        'Home': 'home professor',
        'Ver conteúdos': 'ver conteudo',
        'Criar conteúdo': 'criar conteudo',
        'Editar conteúdo': 'editar conteudo',
        }

    selected = st.sidebar.selectbox('O que deseja fazer hoje?', page_mapping.keys())
    page = page_mapping[selected]

    if st.sidebar.button('Acessar'):
        st.vm.set_page(page)