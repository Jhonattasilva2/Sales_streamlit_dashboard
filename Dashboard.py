import streamlit as st
import requests
import pandas as pd 
import plotly.express as px

url = 'https://labdados.com/produtos'

st.title('DASHBOARD DE VENDAS :shopping_trolley:')

response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

st.dataframe(dados)