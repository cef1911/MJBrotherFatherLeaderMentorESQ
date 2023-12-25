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


st.markdown('<p class="big-font">Merry Christmas, Happy Kwanzaa, and Happy New Year To My Prophyte and Friend Michael Jefferson!!</p>', unsafe_allow_html=True)
st.write("##")
st.markdown('<p class="big-font">"Heartfelt Tribute and Thank You Que, from Chris Franklin"</p>', unsafe_allow_html=True)
st.write("##")



#st.markdown('<p style="font-family:sans-serif; color:Purple; font-size: 42px;">"Omega Man"</p>'

st.markdown('<p class="big-font">Omega Man</p>', unsafe_allow_html=True)
image = Image.open("oppfMJ.jpeg")
st.image(image, caption='Omega Man!!')

st.markdown('<p class="big-font">Sophiscated Voter Advocate</p>', unsafe_allow_html=True)
imagetwo = Image.open("BVoteMJ.jpeg")
st.image(imagetwo, caption='Sophiscated Voter Advocate')

st.markdown('<p class="big-font">Kiyama Movement Creator</p>', unsafe_allow_html=True)
imagethree = Image.open("KMMJ.jpeg")
st.image(imagethree, caption='Kiyama Movement Creator')

st.markdown('<p class="big-font">Author</p>', unsafe_allow_html=True)
imagefour = Image.open("author.jpeg")
st.image(imagefour)

st.markdown('<p class="big-font">Leader and Esquire</p>', unsafe_allow_html=True)
imagefour = Image.open("NHMJ.jpeg")
imagefive = Image.open("ESQ.jpeg")
st.image(imagefour)
st.image(imagefive)


st.balloons()

st.markdown('<p class="big-font">Happy Holidays Prophyte! Chris</p>', unsafe_allow_html=True)
#st.snow()

