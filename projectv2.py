import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if 'data' not in st.session_state:
    df = pd.read_excel(r'C:\Users\user\Downloads\Data science\Python\projeto_chatbot\projeto_pm\veic_produto.xlsx')
    colunas = {'dia':'Dia', 'semana':'Dia da semana', 'hora':'Hora', 'periodo':'Período','mes':'Mês', 'crime':'Crime','cia':'CIA PM', 'endereco':'Endereço',
       'bairro':'Bairro', 'subsetor':'Subsetor', 'cidade':'Cidade', 'data_recuperado':'Data da Recuperação', 'bairro_recuperado':'Bairro da recuperação',
       'ambiente':'Ambiente', 'tipo':'Tipo do veículo', 'marca':'Marca', 'modelo':'Modelo', 'placa':'Placa', 'ano':'Ano','flagrante':'Flagrante?',
       'vitima':'Vítima', 'num_agressores':'N° de agressores', 'sexo':'Sexo dos agressores', 'cor':'Cor', 'arma':'Arma utilizada', 'transporte':'Transporte utilizado',
       'cor_veic':'Cor do veículo utilizado', 'localizado':'Localizado?'}
    df.rename(columns=colunas,inplace=True)
    cia = {'_1ªCIA': '1ªCia', '_2ªCIA':'2ªCia', '_3ªCIA': '3ªCia'}
    df['CIA PM'] = df['CIA PM'].map(cia)

    crime = {'FV': 'Furto', 'RV':'Roubo'}
    df['Crime'] = df['Crime'].map(crime)

    df['Bairro da recuperação']= df['Bairro da recuperação'].fillna('Não Localizado')

    df.fillna({'Localizado?' : 0}, inplace= True)
    loc = {1: 'Sim', 0 : 'Não'}
    df['Localizado?'] = df['Localizado?'].map(loc)

    df.fillna({'Cor do veículo utilizado' : 0}, inplace=True)
    cor_veic = {0: 'N/INF'}
    df['Cor do veículo utilizado'] = df['Cor do veículo utilizado'].map(cor_veic)

    df.fillna({'N° de agressores' : 0}, inplace= True)
    df.fillna({'Sexo dos agressores' : 'N/ INF'}, inplace= True)
    df.fillna({'Cor' : 'N/ INF'}, inplace= True)
    df.fillna({'Arma utilizada' : 'N/ INF'}, inplace= True)
    df.fillna({'Transporte utilizado' : 'N/ INF'}, inplace= True)
    df.fillna({'Cor do veículo utilizado' : 'N/ INF'}, inplace= True)


    st.session_state['data'] = df

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Cidade', 'Crime', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
       'Cor do veículo utilizado']

df = df[colunas]

col1, col2 = st.columns(2)
col1.title('Análise Geocriminal 3° BC')
col2.image(r'C:\Users\user\Downloads\Data science\Python\projeto_chatbot\projeto_pm\3BC.png')
st.header('**Estatísticas anuais**:')
on = st.toggle("Mostrar Dados")
if on:
    st.dataframe(df)

furto1 = df[df['Crime'] == 'Furto']
roubo1 = df[df['Crime'] == 'Roubo']
soma_furto = furto1['Crime'].value_counts().max()
soma_roubo = roubo1['Crime'].value_counts().max()
loc_furto = furto1[furto1['Localizado?'] == 'Sim']['Crime'].value_counts().max()
loc_roubo = roubo1[roubo1['Localizado?'] == 'Sim']['Crime'].value_counts().max()
nloc_furto = furto1[furto1['Localizado?'] == 'Não']['Crime'].value_counts().max()
nloc_roubo = roubo1[roubo1['Localizado?'] == 'Não']['Crime'].value_counts().max()

col1,col2 = st.columns(2)
col1.metric('**Furtos Veiculos**:', soma_furto)
col1.metric('**Furto Veículo Localizado**:', loc_furto)
col1.metric('**Furto Veículo Não localizado**:', nloc_furto)
col2.metric('**Roubo de Veículos**:', soma_roubo)
col2.metric('**Roubo Veículo Localizado**:', loc_roubo)
col2.metric('**Roubo Veículo não localizado**:', nloc_roubo)

st.divider()
st.header('**Estatísticas Mensais**:')

mes = df['mês'].value_counts().index
meses = st.selectbox('Mês', mes)
df_mes = df[df['mês'] == meses]
on = st.toggle("Mostrar Dados Mensais")
if on:
    st.dataframe(df_mes)

furto1 = df_mes[df_mes['Crime'] == 'Furto']
roubo1 = df_mes[df_mes['Crime'] == 'Roubo']
soma_furto = furto1['Crime'].value_counts().max()
soma_roubo = roubo1['Crime'].value_counts().max()
loc_furto = furto1[furto1['Localizado?'] == 'Sim']['Crime'].value_counts().max()
loc_roubo = roubo1[roubo1['Localizado?'] == 'Sim']['Crime'].value_counts().max()
nloc_furto = furto1[furto1['Localizado?'] == 'Não']['Crime'].value_counts().max()
nloc_roubo = roubo1[roubo1['Localizado?'] == 'Não']['Crime'].value_counts().max()
col1,col2 = st.columns(2)
col1.metric(label="Total de Furtos Veículo", value= soma_furto)
col1.metric('Furto Localizados', loc_furto)
col1.metric('**Furto Veículo Não localizado**:', nloc_furto)
col2.metric(label="Total de Roubos Veículo", value= soma_roubo)
col2.metric('Roubos Localizados', loc_roubo)
col2.metric('**Roubo Veículo não localizado**:', nloc_roubo)