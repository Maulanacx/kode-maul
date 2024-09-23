import streamlit as st

x = st.number_input("masukkan angka")
sx = st.text_input("satuan", "C")
st.write("Anda memasukkan", x,' ',sx)
sy = st.text_input("Dikonversi ke", "C")

st.write(x,' ',sx, '= ...', sy)
