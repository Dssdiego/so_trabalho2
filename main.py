# Autor: Diego Santos Seabra

import streamlit as st
from header import header

from fifo import fifo
from lru import lru
from otimo import otimo

display = ("FIFO","LRU","Ótimo")
options = list(range(len(display)))

def main():
    header()
    select = st.selectbox(label='Escolha o que deseja visualizar',options=options, format_func=lambda x: display[x])
    st.write("---------------")

    if select == 0:
        st.write('Algoritmo: **FIFO**')
        fifo()
    
    if select == 1:
        st.write('Algoritmo: **LRU**')
        lru()

    if select == 2:
        st.write('Algoritmo: **Ótimo**')
        otimo()    

if __name__ == '__main__':
    main()