import streamlit as st

from app.controllers.view_manager import ViewManager


@st.cache_resource()
def start_view_manager():
    st.vm = ViewManager()


def main():
    start_view_manager()
    st.vm.run()

if __name__ == "__main__":
    main()
