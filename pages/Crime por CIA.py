import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = st.session_state['data']

colunas = ['mês', 'Dia', 'Dia da semana', 'Hora', 'Período', 'CIA PM', 'Endereço', 'Bairro', 'Subsetor', 'Cidade', 'Crime', 'Objeto', 'Tipo do veículo', 'Marca', 'Modelo', 'Placa', 'Ano',
           'Vítima', 'Flagrante?',  'Localizado?', 'Data da Recuperação', 'Bairro da recuperação', 'Ambiente', 'N° de agressores', 'Sexo dos agressores', 'Cor', 'Arma utilizada', 'Transporte utilizado',
       'Cor do veículo utilizado']

df = df[colunas]

st.title('Indicadores criminais dividos por CIA')

cia = df['CIA PM'].value_counts().index
cias = st.selectbox('Cia', cia)
df_cia = df[df['CIA PM'] == cias]
df_rv= df_cia[df_cia['Crime'] == 'Roubo Veic']
df_fv= df_cia[df_cia['Crime'] == 'Furto Veic']
df_r= df_cia[df_cia['Crime'] == 'Roubo']

on = st.toggle("Mostrar Dados")
col1,col2,col3 = st.columns(3)
if on:
    col1.markdown('**Furto Veic**')
    col1.dataframe(df_fv)
    col2.markdown('**Roubo Veic**')
    col2.dataframe(df_rv)
    col3.markdown("**Roubo Outros**")
    col3.dataframe(df_r)

col1, col2 = st.columns(2)
mes = df_cia['mês'].value_counts().index
meses = col1.selectbox('Mês', mes)
df_mes = df_cia[df_cia['mês'] == meses]
on = col1.toggle("Mostrar Dados mensais")
if on:
    col1.dataframe(df_mes)

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
col1.metric('**Furtos Veiculos**:', soma_furtov)
col1.metric('**Furto Veículo Localizado**:', loc_furto)
col1.metric('**Furto Veículo Não localizado**:', nloc_furto)
col2.metric('**Roubo de Veículos**:', soma_roubov)
col2.metric('**Roubo Veículo Localizado**:', loc_roubo)
col2.metric('**Roubo Veículo não localizado**:', nloc_roubo)
col3.metric('**Roubo Outros**:', soma_roubo)

st.divider()

col1,col2, col3 = st.columns(3)
col1.markdown(f'**Período com mais ocorrências**: {df_mes["Período"].value_counts().index[0]}')
col2.markdown('**Horário com mais ocorrências**:')
col3.markdown(f'**Setor com mais ocorrências**: {df_mes["Subsetor"].value_counts().index[0]}')

st.divider()
st.header('Estatísticas:')
col1,col2,col3 = st.columns(3)
on = col1.toggle('Detalhes Período')
if on:
    peri = df_mes['Período'].value_counts().index
    peris = col1.selectbox('Período', peri)
    df_peri = df_mes[df_mes['Período'] == peris]
    fv = df_peri['Crime'].value_counts().loc['Furto Veic']
    rv = df_peri['Crime'].value_counts().loc['Roubo Veic']
    r = df_peri['Crime'].value_counts().loc['Roubo']
    col1.markdown(f'**Furto Veíc**: {fv}')
    col1.markdown(f'**Roubo Veíc**: {rv}')
    col1.markdown(f'**Roubo outros**: {r}')

on = col2.toggle('Detalhes Setores')
if on:
    set = df_mes['Subsetor'].value_counts().index
    sets = col2.selectbox('Subsetor', set)
    df_set = df_mes[df_mes['Subsetor'] == sets]
    fv = df_set['Crime'].value_counts().loc['Furto Veic']
    rv = df_set['Crime'].value_counts().loc['Roubo Veic']
    r = df_set['Crime'].value_counts().loc['Roubo']
    col2.markdown(f'**Furto Veíc**: {fv}')
    col2.markdown(f'**Roubo Veíc**: {rv}')
    col2.markdown(f'**Roubo outros**: {r}')

st.subheader('**Crimes:**')
crime = df_mes['Crime'].value_counts().index
crimes = st.selectbox('Crime', crime)
df_crime = df_mes[df_mes['Crime'] == crimes]
on = st.toggle("Mostrar")
if on:
    st.dataframe(df_crime[['Dia', 'Dia da semana', 'Hora', 'Período','Crime', 'Endereço', 'Bairro', 'Objeto', 'Tipo do veículo', 'Flagrante?']])
col1,col2,col3,col4 = st.columns(4)
week = df_crime['Dia da semana'].value_counts().index[0]
col1.metric('**Dia da semana com mais ocorrências**:', week)
bairro = df_crime['Bairro'].value_counts().index[0]
col2.metric('**Bairro com mais ocorrências**:', bairro)
periodo = df_crime['Período'].value_counts().index[0]
col3.metric('**Período com mais ocorrências**:', periodo)
amb = df_crime['Ambiente'].value_counts().index[0]
col4.metric('**Ambiente com mais ocorrências**:', amb)
sex = df_crime['Vítima'].value_counts().index[0]
col1.metric('**Maioria de vítimas**:', sex)
obj = df_crime['Objeto'].value_counts().index[0]
col2.metric('**Objetos**:', obj)
tipo = df_crime['Tipo do veículo'].value_counts().index[0]
col3.metric('**Tipo de veículo mais levado**:', tipo)
fla = df_crime['Flagrante?'].value_counts()['Sim']
col4.metric('**Flagrantes**:', fla)
oco = df_crime['Crime'].value_counts().iloc[0]
col1.metric('**Número ocorrências**:', oco)
bairro = df_crime['Bairro'].value_counts().index[0]



#setor = df_mes['Subsetor'].value_counts().index
#setores = st.selectbox('Setor', setor)
#df_setor = df_mes[df_mes['Subsetor'] == setores]
#colunas = ['Dia', 'Dia da semana', 'Hora', 'Período','Endereço', 'Bairro','Crime', 'Flagrante?']
#st.dataframe(df_setor[colunas])

#col1, col2,col3 = st.columns(3)

#col1.markdown('**Endereço com mais ocorrências**:')
#col1.bar_chart(df_setor['Endereço'].value_counts())

#col2.markdown(f'**Período com mais ocorrências no setor**: {df_setor["Período"].value_counts().index[0]}')
#col2.bar_chart(df_setor['Período'].value_counts())
