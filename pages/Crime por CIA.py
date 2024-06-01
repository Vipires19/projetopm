import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Cidade', 'Crime', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
       'Cor do veículo utilizado']

df = df[colunas]

st.title('Indicadores criminais dividos por CIA')

cia = df['CIA PM'].value_counts().index
cias = st.selectbox('Cia', cia)
df_cia = df[df['CIA PM'] == cias]

on = st.toggle("Mostrar Dados")
if on:
    st.dataframe(df_cia)

col1, col2 = st.columns(2)
mes = df_cia['mês'].value_counts().index
meses = col1.selectbox('Mês', mes)
df_mes = df_cia[df_cia['mês'] == meses]
on = col1.toggle("Mostrar Dados mensais")
if on:
    col1.dataframe(df_mes)

furto1 = df_mes[df_mes['Crime'] == 'Furto']
roubo1 = df_mes[df_mes['Crime'] == 'Roubo']
soma_furto = furto1['Crime'].value_counts().max()
soma_roubo = roubo1['Crime'].value_counts().max()
loc_furto = furto1[furto1['Localizado?'] == 'Sim']['Crime'].value_counts().max()
loc_roubo = roubo1[roubo1['Localizado?'] == 'Sim']['Crime'].value_counts().max()
nloc_furto = furto1[furto1['Localizado?'] == 'Não']['Crime'].value_counts().max()
nloc_roubo = roubo1[roubo1['Localizado?'] == 'Não']['Crime'].value_counts().max()


col1, col2, col3 = st.columns(3)
col1.metric(label="Total de Furtos Veículo", value= soma_furto)
col2.metric('Furto Localizados', loc_furto)
col3.metric('**Furto Veículo Não localizado**:', nloc_furto)

col1.metric(label="Total de Roubos Veículo", value= soma_roubo)
col2.metric('Roubos Localizados', loc_roubo)
col3.metric('**Roubo Veículo não localizado**:', nloc_roubo)

st.divider()

col1,col2, col3 = st.columns(3)
col1.markdown(f'**Período de maior incidência**: {df_mes["Período"].value_counts().index[0]}')
col1.bar_chart(df_mes['Período'].value_counts())
col2.markdown('**Horário com mais ocorrências**:')
col2.bar_chart(df_mes['Hora'].value_counts())
col3.markdown(f'**Setor com mais ocorrências**: {df_mes["Subsetor"].value_counts().index[0]}')
col3.bar_chart(df_mes['Subsetor'].value_counts())

st.divider()
st.header('Indicadores do setor')

setor = df_mes['Subsetor'].value_counts().index
setores = st.selectbox('Setor', setor)
df_setor = df_mes[df_mes['Subsetor'] == setores]
colunas = ['Dia', 'Dia da semana', 'Hora', 'Período','Endereço', 'Bairro','Crime', 'Flagrante?']
st.dataframe(df_setor[colunas])

col1, col2,col3 = st.columns(3)

col1.markdown('**Endereço com mais ocorrências**:')
col1.bar_chart(df_setor['Endereço'].value_counts())

col2.markdown(f'**Período com mais ocorrências no setor**: {df_setor["Período"].value_counts().index[0]}')
col2.bar_chart(df_setor['Período'].value_counts())

