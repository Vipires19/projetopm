import streamlit as st
import pandas as pd
import webbrowser

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Crime', 'Cidade', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
           'Cor do veículo utilizado']

df = df[colunas]

st.title('**Roubo de Veículos 3° BC**')

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Crime', 'Cidade', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?']
df_rv = df[df['Crime'] == 'Roubo']
df_rv = df_rv[colunas]
df_rv

col1,col2,col3 = st.columns(3)
mes = df['mês'].value_counts().index
meses = col1.selectbox('Mês', mes)
df_mes = df[df_mes['mês'] == meses]
tipos = df_mes['Tipo do veículo'].value_counts().index
tipo = col1.selectbox('Tipo do veículo', tipos)
df_tipo = df_mes[df_mes['Tipo do veículo'] == tipo]


