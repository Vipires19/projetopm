import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

#sns.set_theme(style="darkgrid")
#fig = plt.subplots(figsize=(6, 15))

#sns.set_color_codes("pastel")
#GRAPH = sns.barplot(x= 'CIA PM', y= 'Crime', data=df_mes,
#            label="Total", color="b")
#sns.despine(left=True, bottom=True)

#st.pyplot(GRAPH)
# Plot the crashes where alcohol was involved
#sns.set_color_codes("muted")
#ns.barplot(x="alcohol", y="abbrev", data=crashes,
#            label="Alcohol-involved", color="b")

# Add a legend and informative axis label
#ax.legend(ncol=2, loc="lower right", frameon=True)
#ax.set(xlim=(0, 24), ylabel="",
#       xlabel="Automobile collisions per billion miles")



