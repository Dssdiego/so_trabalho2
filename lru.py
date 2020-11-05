import streamlit as st
import pandas as pd

def lru():
    num_faltas = 0
    f = []
    stt = []

    num_quadros = st.number_input(label='Número de Quadros', step=1, value=3, min_value=0, max_value=20)
    string = st.text_input(label='Sequência de Acesso', value="7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1")

    s = list(map(int, string.strip().split()))

    refs = []
    hits = []
    quadros = []

    st.write('Resultado:')

    g = globals()
    for i in range(num_quadros):
        g['q{0}'.format(i+1)] = []

    # Para cada página da sequência de processos
    for i in s:
        refs.append(i)
        # Se a página não está no array
        if i not in f:
            # Se há disponibilidade no array, adiciona uma página
            # Mantém o índice da página menos recentemente utilizada (LRU)
            if(len(f) < num_quadros):
                f.append(i)
                stt.append(len(f)-1)
            # Mantém o índice de cada página
            else:
                ind = stt.pop(0)
                f[ind] = i
                stt.append(ind)
            # Incrementa a falta de página
            num_faltas += 1
            hits.append('Sim')
        # "Hit"
        # Substitui a página atual pela página menos recentemente utilizada (LRU)
        else:
            stt.append(stt.pop(stt.index(f.index(i))))
            hits.append('Não')

        # Preenche os quadros
        for x in f:
            quadros.append(x)
        for x in range(num_quadros-len(f)):
            quadros.append(None)

    # Cria os arrays de quadro
    q_cont = 0
    for i in range(len(quadros)):
        if q_cont == num_quadros:
            q_cont = 0
        
        if quadros[i] == None:
            g['q{0}'.format(q_cont+1)].append('')
        else:
            g['q{0}'.format(q_cont+1)].append(quadros[i])
        q_cont += 1

    # Cria o índice da tabela
    index = []
    index.append('Página')
    for i in range(num_quadros):
        index.append('Q' + str(i+1))

    index.append('Falta?')

    # Cria as linhas
    linhas = []
    linhas.append(refs)
    for i in range(num_quadros):
        linhas.append(g['q{0}'.format(i+1)])
    linhas.append(hits)

    # Cria a tabela
    df = pd.DataFrame(linhas, index=index)
    st.dataframe(df.style.applymap(cor_falta_pagina))

    st.write('**Faltas de Página:** ' + str(num_faltas))
    st.write('**Total de Páginas:** ' + str(len(s)))

def cor_falta_pagina(value):
  if value is 'Não':
    color = 'red'
  elif value is 'Sim':
    color = 'green'
  else:
    color = 'black'

  return 'color: %s' % color