import streamlit as st

x = st.number_input("masukkan angka")
sx = st.text_input("satuan", "c")
st.write("Anda memasukkan", x,' ',sx)
