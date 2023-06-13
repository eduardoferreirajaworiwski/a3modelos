"""
Controlador de views
Essa classe é responsável por gerenciar as views do sistema, ela é responsável por chamar a view correta de acordo com o estado atual do sistema.
"""

import streamlit as st
from app.views.preauth import home_preauth
from app.views.login_professor import show_login_page
from app.views.home_professor import home_professor
from app.views.conteudos_create import conteudos_create_page
from app.views.conteudos_view import conteudos_view_page
from app.views.conteudos_edit import conteudos_edit_page

class ViewManager:
    def __init__(self):
        self.pages = {
            "preauth": home_preauth,
            "login professor": show_login_page,
            "home professor": home_professor,
            'criar conteudo': conteudos_create_page,
            'editar conteudo': conteudos_edit_page,
            'ver conteudo': conteudos_view_page,
        }

        self.current_page = self.pages["preauth"]

    def set_page(self, page_name):
        self.current_page = self.pages[page_name]
        st.experimental_rerun()

    def run(self):
        self.current_page()