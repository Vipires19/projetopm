import streamlit as st
import pandas as pd

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
df_mes = df[df['mês'] == meses]
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
#tipe = list(df_ocr['Tipo do veículo'])
#placa = list(df_ocr['Placa'])
ocr = list(df_veic['Endereço'])[0]
col1.markdown(f'**Endereço da ocorrência**: {ocr}')
bairro = list(df_veic["Bairro"])[0]
col2.markdown(f'**Bairro**: {bairro}')
sector = list(df_veic['Subsetor'])[0].split('.')[-1]
col3.markdown(f'**Setor**: {sector}')
fla = list(df_veic['Flagrante?'])[0]
col4.markdown(f'**Flagrante?**: {fla}')

st.header('**Ocorrência**')
col1,col2,col3 = st.columns(3)
vit = list(df_veic['Vítima'])[0]
col1.markdown(f'**Vítima**: {vit}')
ladrao = list(df_veic['N° de agressores'])[0]
col2.markdown(f'**N° de agressores**: {ladrao}')
se = list(df_veic['Sexo dos agressores'])[0]
col3.markdown(f'**Sexo dos agressores**: {se}')
clad = list(df_veic['Cor'])[0]
col1.markdown(f'**Cor**: {clad}')
gun = list(df_veic['Arma utilizada'])[0]
col2.markdown(f'**Arma utilizada**: {gun}')
trans = list(df_veic['Transporte utilizado'])[0]
col3.markdown(f'**Transporte utilizado**: {trans}')
cvu = list(df_veic['Cor do veículo utilizado'])[0]
col1.markdown(f'**Cor do veículo utilizado**: {cvu}')

st.header('**Localização:**')
col1,col2,col3 = st.columns(3)
locd = list(df_veic['Localizado?'])[0]
col1.markdown(f'**Localizado?**: {locd}')
data_rec = list(df_veic['Data da Recuperação'])[0].date()
col2.markdown(f'**Data da localização**: {data_rec}')
recu = list(df_veic['Bairro da recuperação'])[0]
col3.markdown(f'**Bairro da localização**: {recu}')

