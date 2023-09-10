import streamlit as st
from PIL import Image

#asset
img_contact_f = Image.open("C:/Users/Jacob/Desktop/New/new/image/seth.jpg")

st.title("Seth Eli J Bangar")

with st.container():
    st.write("---")
    st.header("Paano ngaba maging maaral na istudyante? ")
    st.write("##")
    image_c, text_c = st.columns((1, 2))
    with image_c:
        st.image(img_contact_f)
    with text_c:
        st.subheader("Kita mo yan? ganyan")
        st.write(
        """
        pangalan nyan seth eli bangad allias seth eli bangar
        
        dating baliko kamay
        
        maples ya umbatik
        
        mankukugip ed klase
        
        """
        )