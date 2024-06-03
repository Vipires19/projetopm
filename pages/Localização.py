import streamlit as st
import pandas as pd

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Crime', 'Cidade', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
           'Cor do veículo utilizado']

df = df[colunas]

st.title('**Localização de caráter geral**')

colunas = ['CIA PM', 'mês', 'Bairro', 'Bairro da recuperação', 'Ambiente', 'Crime', 'Cidade', 'Tipo do veículo', 'Marca','Modelo', 'Placa', 'Ano',  'Localizado?']
df_loc = df[df['Localizado?'] == 'Sim']
df_loc = df_loc[colunas]
on = st.toggle("Mostrar Dados")
if on:
    st.dataframe(df_loc)

col1,col2,col3 = st.columns(3)
mes = df_loc['mês'].value_counts().index
meses = col1.selectbox('Mês', mes)
df_mes = df_loc[df_loc['mês'] == meses]

cia = df_mes['CIA PM'].value_counts().index
cias = col2.selectbox('Cia', cia)
df_cia = df_mes[df_mes['CIA PM'] == cias]
on = st.toggle('Dados')
if on:
    st.dataframe(df_cia)

st.divider()
st.header('**Bairros**')
colunas = ['CIA PM', 'mês', 'Dia', 'Endereço', 'Bairro', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'Crime', 'Tipo do veículo', 'Modelo', 'Placa', 'Ano',
           'Flagrante?',  'Localizado?']
df_loc_set = df[df['Localizado?'] == 'Sim']
df_loc_set = df_loc_set[colunas]

#col1,col2,col3 = st.columns(3)
#cia = df_loc_set['CIA PM'].value_counts().index
#cias = col1.selectbox('Cia', cia)
#df_cia = df_loc_set[df_loc_set['CIA PM'] == cias]
bairro = df_cia['Bairro'].value_counts().index
bairros = st.selectbox('Bairro', bairro)
df_bairro = df_cia[df_cia['Bairro'] == bairros]
df_bairro[['mês', 'Dia', 'Hora', 'Endereço', 'Bairro', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'Crime', 'Cidade', 'Tipo do veículo', 'Modelo', 'Placa', 'Ano',
           'Flagrante?']]
#tipo = df_mes['Tipo do veículo'].value_counts().index
#tipos = col2.selectbox('Tipo do veículo', tipo)
#df_tipo = df_mes[df_mes['Tipo do veículo'] == tipos]

#veic = df_tipo['Placa'].value_counts().index
#veics = col3.selectbox('Veículo', veic)
#df_veic = df_tipo[df_tipo['Placa'] == veics]
