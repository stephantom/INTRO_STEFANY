import streamlit as st
from PIL import Image

st.title(" Mi primer App!!")

st.header ("En este espacio empiezo a desarrollar...")
st.write("Facilmente puedo..")
Image = Image.open("Fondo de Pantalla de Escritorio Motivational en Rojo Carbón estilo Antidiseño.png")

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo','Este es mi texto')
st.write('El texto escrito es', texto)

