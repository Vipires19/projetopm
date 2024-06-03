import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if 'data' not in st.session_state:
    df = pd.read_excel(r'veic_produto.xlsx')
    colunas = {'dia':'Dia', 'semana':'Dia da semana', 'hora':'Hora', 'periodo':'Período','mes':'Mês', 'crime':'Crime','cia':'CIA PM', 'endereco':'Endereço',
       'bairro':'Bairro', 'subsetor':'Subsetor', 'cidade':'Cidade', 'data_recuperado':'Data da Recuperação', 'bairro_recuperado':'Bairro da recuperação',
       'ambiente':'Ambiente', 'tipo':'Tipo do veículo', 'marca':'Marca', 'modelo':'Modelo', 'placa':'Placa', 'ano':'Ano','flagrante':'Flagrante?',
       'vitima':'Vítima', 'num_agressores':'N° de agressores', 'sexo':'Sexo dos agressores', 'cor':'Cor', 'arma':'Arma utilizada', 'transporte':'Transporte utilizado',
       'cor_veic':'Cor do veículo utilizado', 'localizado':'Localizado?', 'objeto_quem': 'Objeto'}
    
    df.rename(columns=colunas,inplace=True)

    cia = {'_1ªCIA': '1ªCia', '_2ªCIA':'2ªCia', '_3ªCIA': '3ªCia'}
    df['CIA PM'] = df['CIA PM'].map(cia)

    crime = {'FV': 'Furto Veic', 'RV':'Roubo Veic', 'RO':'Roubo'}
    df['Crime'] = df['Crime'].map(crime)
    
    df['Bairro da recuperação']= df['Bairro da recuperação'].fillna('Não Localizado')

    df.fillna({'Localizado?' : 0}, inplace= True)
    loc = {1: 'Sim', 0 : 'Não'}
    df['Localizado?'] = df['Localizado?'].map(loc)

    df.fillna({'Cor do veículo utilizado' : 0}, inplace=True)
    cor_veic = {0: 'N/INF'}
    df['Cor do veículo utilizado'] = df['Cor do veículo utilizado'].map(cor_veic)

    df.fillna({'N° de agressores' : 'N/ INF'}, inplace= True)
    df.fillna({'Sexo dos agressores' : 'N/ INF'}, inplace= True)
    df.fillna({'Cor' : 'N/ INF'}, inplace= True)
    df.fillna({'Arma utilizada' : 'N/ INF'}, inplace= True)
    df.fillna({'Transporte utilizado' : 'N/ INF'}, inplace= True)
    df.fillna({'Cor do veículo utilizado' : 'N/ INF'}, inplace= True)
    df.fillna({'Tipo do veículo' : 'N/ INF'}, inplace= True)
    df.fillna({'Marca' : 'N/ INF'}, inplace= True)
    df.fillna({'Modelo' : 'N/ INF'}, inplace= True)
    df.fillna({'Placa' : 'N/ INF'}, inplace= True)
    df.fillna({'Ano' : 'N/ INF'}, inplace= True)
    df.fillna({'Objeto' : 'N/ INF'}, inplace= True)


    st.session_state['data'] = df

st.set_page_config(
    layout =  'wide',
    page_title = 'Análise Geocriminal 3° BC',
)

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Cidade', 'Crime', 'Objeto', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
       'Cor do veículo utilizado']

df = df[colunas]

col1, col2 = st.columns(2)
col1.title('Análise Geocriminal 3° BC')
col2.image(r'3BC.png')
st.header('**Estatísticas anuais**:')
df_rv= df[df['Crime'] == 'Roubo Veic']
df_fv= df[df['Crime'] == 'Furto Veic']
df_r= df[df['Crime'] == 'Roubo']



on = st.toggle("Mostrar Dados")
col1,col2,col3 = st.columns(3)
if on:
    col1.markdown('**Furto Veic**')
    col1.dataframe(df_fv)
    col2.markdown('**Roubo Veic**')
    col2.dataframe(df_rv)
    col3.markdown("**Roubo Outros**")
    col3.dataframe(df_r)

furtov = df[df['Crime'] == 'Furto Veic']
roubov = df[df['Crime'] == 'Roubo Veic']
roubo = df[df['Crime'] == 'Roubo']
soma_furtov = furtov['Crime'].value_counts().max()
soma_roubov = roubov['Crime'].value_counts().max()
soma_roubo = roubo['Crime'].value_counts().max()
loc_furto = furtov[furtov['Localizado?'] == 'Sim']['Crime'].value_counts().max()
loc_roubo = roubov[roubov['Localizado?'] == 'Sim']['Crime'].value_counts().max()
nloc_furto = furtov[furtov['Localizado?'] == 'Não']['Crime'].value_counts().max()
nloc_roubo = roubov[roubov['Localizado?'] == 'Não']['Crime'].value_counts().max()

col1,col2,col3 = st.columns(3)
col1.metric('**Furtos Veiculos**:', soma_furtov)
col1.metric('**Furto Veículo Localizado**:', loc_furto)
col1.metric('**Furto Veículo Não localizado**:', nloc_furto)
col2.metric('**Roubo de Veículos**:', soma_roubov)
col2.metric('**Roubo Veículo Localizado**:', loc_roubo)
col2.metric('**Roubo Veículo não localizado**:', nloc_roubo)
col3.metric('**Roubo Outros**:', soma_roubo)

#############################################################################################################################################################

st.divider()
st.header('**Estatísticas Mensais**:')

mes = df['mês'].value_counts().index
meses = st.selectbox('Mês', mes)
df_mes = df[df['mês'] == meses]
df_rv_mes= df_mes[df_mes['Crime'] == 'Roubo Veic']
df_fv_mes= df_mes[df_mes['Crime'] == 'Furto Veic']
df_r_mes= df_mes[df_mes['Crime'] == 'Roubo']


on = st.toggle("Mostrar Dados Mensais")
col1,col2,col3 = st.columns(3)
if on:
    col1.markdown('**Furto Veic**')
    col1.dataframe(df_fv_mes)
    col2.markdown('**Roubo Veic**')
    col2.dataframe(df_rv_mes)
    col3.markdown('**Roubo Outros**')
    col3.dataframe(df_r_mes)

furtov = df_mes[df_mes['Crime'] == 'Furto Veic']
roubov = df_mes[df_mes['Crime'] == 'Roubo Veic']
roubo = df_mes[df_mes['Crime'] == 'Roubo']
soma_furtov = furtov['Crime'].value_counts().max()
soma_roubov = roubov['Crime'].value_counts().max()
soma_roubo = roubo['Crime'].value_counts().max()
loc_furto = furtov[furtov['Localizado?'] == 'Sim']['Crime'].value_counts().max()
loc_roubo = roubov[roubov['Localizado?'] == 'Sim']['Crime'].value_counts().max()
nloc_furto = furtov[furtov['Localizado?'] == 'Não']['Crime'].value_counts().max()
nloc_roubo = roubov[roubov['Localizado?'] == 'Não']['Crime'].value_counts().max()
col1,col2,col3 = st.columns(3)
col1.metric(label="Total de Furtos Veículo", value= soma_furtov)
col1.metric('Furto Localizados', loc_furto)
col1.metric('**Furto Veículo Não localizado**:', nloc_furto)
col2.metric(label="Total de Roubos Veículo", value= soma_roubov)
col2.metric('Roubos Localizados', loc_roubo)
col2.metric('**Roubo Veículo não localizado**:', nloc_roubo)
col3.metric('**Roubo Outros**:', soma_roubo)
