import streamlit as st
import pandas as pd

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Crime', 'Cidade', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
           'Cor do veículo utilizado']

df = df[colunas]

st.title('**Localização de caráter geral**')

colunas = ['CIA PM', 'mês', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'Crime', 'Cidade', 'Vítima', 'Tipo do veículo', 'Marca','Modelo', 'Placa', 'Ano',
           'Flagrante?',  'Localizado?']
df_loc = df[df['Localizado?'] == 'Sim']
df_loc = df_loc[colunas]
on = st.toggle("Mostrar Dados")
if on:
    st.dataframe(df_loc)

col1,col2,col3 = st.columns(3)
mes = df_loc['mês'].value_counts().index
meses = col1.selectbox('Mês', mes)
df_mes = df_loc[df_loc['mês'] == meses]

tipo = df_mes['Tipo do veículo'].value_counts().index
tipos = col2.selectbox('Tipo do veículo', tipo)
df_tipo = df_mes[df_mes['Tipo do veículo'] == tipos]

veic = df_tipo['Placa'].value_counts().index
veics = col3.selectbox('Veículo', veic)
df_veic = df_tipo[df_tipo['Placa'] == veics]

st.divider()
st.header('**Veículo**')
col1,col2,col3,col4 = st.columns(4)
car = list(df_veic['Modelo'])[0]
col1.markdown(f'**Veículo levado**: {car}')
placa = list(df_veic['Placa'])
car_num = placa[0].split(placa[0][2])[1]
car_let = placa[0].split(placa[0][3])[0]
placa = car_let + '-' + car_num
col2.markdown(f'**Placas**: {placa}')
year = list(df_veic['Ano'])[0]
col3.markdown(f'**Ano**: {year}')
mar = list(df_veic['Marca'])[0]
col4.markdown(f'**Marca**: {mar}')
fla = list(df_veic['Flagrante?'])[0]
col4.markdown(f'**Flagrante?**: {fla}')
vit = list(df_veic['Vítima'])[0]
col1.markdown(f'**Vítima**: {vit}')


st.header('**Localização:**')
col1,col2,col3 = st.columns(3)
locd = list(df_veic['Localizado?'])[0]
col1.markdown(f'**Localizado?**: {locd}')
data_rec = list(df_veic['Data da Recuperação'])[0].date()
col2.markdown(f'**Data da localização**: {data_rec}')
recu = list(df_veic['Bairro da recuperação'])[0]
col3.markdown(f'**Bairro da localização**: {recu}')

st.divider()
st.header('**Bairros**')
colunas = ['CIA PM', 'mês', 'Dia', 'Hora', 'Endereço', 'Bairro', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'Crime', 'Cidade', 'Tipo do veículo', 'Modelo', 'Placa', 'Ano',
           'Flagrante?',  'Localizado?']
df_loc_set = df[df['Localizado?'] == 'Sim']
df_loc_set = df_loc_set[colunas]

col1,col2,col3 = st.columns(3)
cia = df_loc_set['CIA PM'].value_counts().index
cias = col1.selectbox('Cia', cia)
df_cia = df_loc_set[df_loc_set['CIA PM'] == cias]
bairro = df_cia['Bairro'].value_counts().index
bairros = col2.selectbox('Bairro', bairro)
df_bairro = df_cia[df_cia['Bairro'] == bairros]
df_bairro[['mês', 'Dia', 'Hora', 'Endereço', 'Bairro', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'Crime', 'Cidade', 'Tipo do veículo', 'Modelo', 'Placa', 'Ano',
           'Flagrante?']]
#tipo = df_mes['Tipo do veículo'].value_counts().index
#tipos = col2.selectbox('Tipo do veículo', tipo)
#df_tipo = df_mes[df_mes['Tipo do veículo'] == tipos]

#veic = df_tipo['Placa'].value_counts().index
#veics = col3.selectbox('Veículo', veic)
#df_veic = df_tipo[df_tipo['Placa'] == veics]