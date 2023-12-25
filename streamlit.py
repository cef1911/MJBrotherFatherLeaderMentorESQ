import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
from PIL import Image



st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:75px !important;
}
</style>
""", unsafe_allow_html=True)

#st.markdown('<p class="big-font">Merry Christmas To Stacey Franklin!!</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">Merry Christmas, Happy Kwanzaa, and Happy New Year To My Prophyte and Friend Michael Jefferson!!</p>', unsafe_allow_html=True)
st.write("##")
st.markdown('<p class="big-font">"Heartfelt Tribute and Thank You Que, from Chris Franklin"</p>', unsafe_allow_html=True)
st.write("##")

oppfMJ = '<p style="font-family:sans-serif; color:Purple; font-size: 42px;">"Omega Man"</p>'
image = Image.open("oppfMJ.PNG")
oppfMJ = '<p style="font-family:sans-serif; color:Purple; font-size: 42px;">"Omega Man"</p>'
st.markdown(oppfMJ, unsafe_allow_html=True)
#st.image(image, channels="BGR")

#image = Image.open("twistedpizzasf.PNG")

#st.image(image, caption='Stacey Franklin, Merry Christmas 2023')

#st.write("Tribute To Stacey Franklin")


# imagetwo = Image.open("birthday.jpeg")

# st.image(imagetwo, caption='Amanda Franklin')


#imagethree = Image.open("memories.png")

#st.image(imagethree, caption='Stacey Franklin')


#st.write("Love You Stacey, Chris")

st.balloons()

st.snow()

#col1, col2, col3 = st.columns(3)

#with col1:
   #st.header("Michael Jefferson Que")
   #st.image("oppfMJ.jpeg")

#with col2:
   #st.header("A dog")
   #st.image("https://static.streamlit.io/examples/dog.jpg")

#with col3:
   #st.header("An owl")
   #st.image("https://static.streamlit.io/examples/owl.jpg")
