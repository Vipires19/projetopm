import streamlit as st
#from deepface import DeepFace
#import cv2
#import os
import streamlit_authenticator as stauth
from pymongo import MongoClient
import urllib
import urllib.parse
from datetime import datetime
import pandas as pd
from collections import Counter
import pytz

st.set_page_config(
            layout =  'wide',
            page_title = 'Fotocrim',
        )
mongo_user = st.secrets['MONGO_USER']
mongo_pass = st.secrets["MONGO_PASS"]

username = urllib.parse.quote_plus(mongo_user)
password = urllib.parse.quote_plus(mongo_pass)
client = MongoClient("mongodb+srv://%s:%s@cluster0.gjkin5a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" % (username, password), ssl = True)
st.cache_resource = client
db = client.fotocrim
coll = db.individual
coll2 = db.cadastro
coll3 = db.abordagens
coll4 = db.usuarios

# --- Authentication ---
# Load hashed passwords

user = coll4.find({})
users = []
for item in user:
    item.pop('_id', None)
    users.append(item)

usuarios = {'usernames' : {}}
for item in users:
    usuarios['usernames'][item['username']] = {'name' : item['name'], 'password' : item['password'][0]}
  
credentials = usuarios

authenticator = stauth.Authenticate(credentials= credentials, cookie_name= 'random_cookie_name', cookie_key='key123', cookie_expiry_days= 1)
authenticator.login()

def alimentando_banco():
    uploaded_files = st.file_uploader(
    "Escolha uma imagem", accept_multiple_files=False)
    nome = st.text_input('Nome do indivíduo:')
    nome_bd = nome.upper()

    if uploaded_files is not None:
        bytes_data = uploaded_files.getvalue()
        ladrao = {'Nome' : nome_bd,
              'Foto' : bytes_data}

    col1,col2,col3,col4 = st.columns(4)
    documento = ['RG', 'CPF', 'MATRICULA']
    doc = col1.selectbox('Documento', documento)
    docs = col1.text_input('N° Documento')
    mae = col2.text_input('Nome da mãe').upper()
    pai = col2.text_input('Nome do pai').upper()
    vulgo = col2.text_input('Vulgo').upper()
    nascimento = col3.text_input('Data de nascimento', placeholder='Ex: 12/12/2024')
    endereco = col4.text_input('Endereço').upper()
    bairro = col4.text_input('Bairro').upper()
    cidade = col4.text_input('Cidade').upper()
    
    cadastro = {'Nome' : nome_bd,
                'Documentos' : {doc : docs},
                'Mae' : mae,
                'Pai' : pai,
                'Vulgo' : vulgo,
                'Nascimento' : nascimento,
                'Endereço' : endereco,
                'Bairro' : bairro,
                'Cidade' : cidade}

    upload = st.button('Salvar')    
    if upload:
       coll.insert_many([ladrao])
       coll2.insert_many([cadastro])

def selecionando_individuo():
    cidade = coll2.find({})
    cidades = []
    for item in cidade:
        item.pop('_id', None)
        cidades.append(item.get('Cidade'))

    lista = Counter(cidades)
    lista_cidades = []
    for i in lista.keys():
        lista_cidades.append(i)

    city = st.selectbox('Cidade para pesquisa', lista_cidades)
    
    nome = coll2.find({'Cidade': city})
    nomes = []
    for item in nome:
        item.pop('_id', None)
        nomes.append(item.get('Nome'))

    name = st.selectbox('Nome para pesquisa', nomes)

    individuo = coll.find({'Nome' : name})
    imagem = []
    for item in individuo:
        item.pop('_id', None)
        imagem.append(item.get('Foto'))

    individuo = coll2.find({'Nome' : name})
    cadastro = []
    for item in individuo:
        item.pop('_id', None)
        cadastro.append(item)

    #individuo = coll.find({})
    #individuos = []
    #for item in individuo:
    #    item.pop('_id', None)
    #    individuos.append(item)
    #imagem = individuos[0].get('Foto')

    col1,col2,col3 = st.columns(3)
    col1.image(imagem,width= 300)
    col2.metric('Nome', cadastro[0].get('Nome'))
    col2.metric('Nome da mãe', cadastro[0].get('Mae'))
    col2.metric('Nome da pai', cadastro[0].get('Pai'))
    col2.metric('Vulgo', cadastro[0].get('Vulgo'))
    col2.metric('Data de nascimento', cadastro[0].get('Nascimento'))
    col3.markdown('Documentos')
    documentos = [cadastro[0].get('Documentos')]
    col3.dataframe(pd.DataFrame(documentos, index = [len([cadastro[0].get('Documento')])]))
    st.metric('Endereço', cadastro[0].get('Endereço'))
    st.metric('Bairro', cadastro[0].get('Bairro'))
    st.metric('Cidade', cadastro[0].get('Cidade'))

    log_abordagens(name)

def abordagens():
    fuso_horario_brasilia = pytz.timezone("America/Sao_Paulo")
    nome = coll2.find({})
    nomes = []
    for item in nome:
        item.pop('_id', None)
        nomes.append(item.get('Nome'))
    name = st.selectbox('Nome do abordado', nomes)
    endereco = st.text_input('Endereço da abordagem')
    cidade = st.text_input('Cidade da abordagem')
    equipe = st.text_input('Equipe que realizou a abordagem', placeholder='Ex. I-00000')
    st.divider()
    st.markdown('Abordagem')
    info = st.text_input('Informação:', placeholder= 'Ex. Indivíduo suspeito de patricar furto de Hilux com veículo xxx-0000')

    abordagem = {'Nome' : name,
                 'Endereço' : endereco,
                 'Cidade' : cidade,
                 'Equipe' : equipe,
                 'Informação' : info}
    
    registro = st.button('Registrar')
    if registro:
        tempo_agora = datetime.now(fuso_horario_brasilia)
        data_utc = tempo_agora
        if isinstance(data_utc, datetime):
            data_brasilia = data_utc.astimezone(fuso_horario_brasilia)
            tempo_agora = data_brasilia.strftime('%d/%m/%Y')
        abordagem.update({'Data abordagem' : tempo_agora})
        coll3.insert_many([abordagem])
    
def log_abordagens(name):
    individuo = coll3.find({'Nome' : name})
    registro_abordagens = []
    for item in individuo:
        item.pop('_id', None)
        registro_abordagens.append(item)

    container = st.container(border=True)
    with container:
        if registro_abordagens == []:
            pass
        else:
            pd.DataFrame(registro_abordagens)[['Data da abordagem', 'Endereço', 'Cidade', 'Equipe', 'Informação']]

def pagina_principal():
    st.title('*FOTOCRIM SÃO PAULO*')
    col1,col2 = st. columns(2)
    col1.image('Caveira.jpg')
    col2.image('BTL.png',width= 400)
    
    st.divider()

    btn = authenticator.logout()
    if btn:
        st.session_state["authentication_status"] == None
        
    tab1,tab2,tab3,tab4 = st.tabs(['Pesquisa Individual', 'Banco de dados', 'Abordagens', 'Foto reconhecimento'])
    
    with tab1:
        st.title('Pesquisa Individual')
        st.markdown('**Aqui você tem acesso a pesquisa de indivíduos cadastrados no banco, onde é possível verificar os dados bem como cadastrar novas informações**')
        selecionando_individuo()

    with tab2:
        st.title('Banco de dados')
        st.markdown('**Aqui é possível ter acesso as fotos dos indivíduos. Só serão admitidas fotos padronizadas para maior facilidade no manuseio do banco bem como na parte de reconhecimento facial**')
        alimentando_banco()

    with tab3:
        st.title('Abordagens')
        st.markdown('**Aqui é o local destinado a registrar informações importantes oriundas de abordagens a indivíduos já cadastrados no banco de dados, afim de criar um mapeamento das possíveis ações criminosas do suspeito**')
        abordagens()

    with tab4:
        st.title('Foto Reconhecimento')
        st.markdown('Local para realizar a comparação de imagens, por exemplo de uma filmagem de furto a residencia, com os suspeitos já cadastrados no nosso banco de dados')
        st.header('Função em construção, em breve mais informações')        

def main():
    if st.session_state["authentication_status"]:
        pagina_principal()
    elif st.session_state["authentication_status"] == False:
        st.error("Username/password is incorrect.")

    elif st.session_state["authentication_status"] == None:
        st.warning("Please insert username and password")

if __name__ == '__main__':
    main()
